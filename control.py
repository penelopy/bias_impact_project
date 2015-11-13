import random
import math

"""A bias simulation based on "Male-Female Differences: A Computer Simulation" from the Feb, 1996 issue of American Psychologist.
 	
	http://www.ruf.rice.edu/~lane/papers/male_female.pdf"""

#TODO Consider other approaches - besides having global variables
NUM_SIMULATIONS = 1
NUM_POSITIONS_LIST = [50, 30, 12] #update once code is working
NUM_LEVELS = len(NUM_POSITIONS_LIST)
ATTRITION = 15
ITERATIONS_PER_SIMULATION = 1
PROMOTION_BIAS = 1

class Employee:
	def __init__(self, gender):
		self.gender = gender
		self.rating = 1

class Averager:
	def __init__(self):
		self.numbers = []

	def add(self, n):
		self.numbers.append(n)

	def get_average(self):
		return self.get_total()/len(self.numbers)

	def get_total(self):
		total = 0
		for n in self.numbers:
			total += n

		return total

class Result:
	# Each element in the array holds the number of men at that level.

	def __init__(self, men, women):
		self.men = men  #this is an array
		self.women = women #this is an array


class Simulation:
	def __init__(self):
		self.levels_to_employees = {}

		for i in range(0, NUM_LEVELS): #set up dictionary, with Key:Level, Value:Empty List of Employees
			self.levels_to_employees[i] = []
		self.hire() #Populates Employees lists in dictionary 50/50 with male/female employees

	# Counts number of men and women at each level and saves totals to num_men or num_women lists
	def get_result(self):
		num_men = []
		num_women = []

		for i in range(NUM_LEVELS):
			num_men.append(0)
			num_women.append(0)

		for level in range(0, NUM_LEVELS):
			# for level, employees in self.levels_to_employees.items():
			employee_list = self.levels_to_employees.get(level)
			if employee_list is not None:
				for employee in employee_list:
					if employee.gender == "male": 
						num_men[level] += 1
					else:
						num_women[level] += 1	
		print "num_women", num_women #something isn't working here
		print "num_men", num_men
		return Result(num_men, num_women)

	#Looks at each employee object in dictionary, checks gender and gives random performance rating
	def talent_review(self):
		for employee_list in self.levels_to_employees.values():	
			for employee in employee_list:
				if employee.gender == "female": 
					employee.rating = random.randint(0, 100)
				else:
					employee.rating = random.randint(0, 100 + PROMOTION_BIAS)


	# Completes dictionary by adding employees at each hiring level
	def hire(self):
		gender = ['male', 'female']
		next_gender = random.choice(gender) #randomly assign gender to first employee
		level = 0
		for positions in NUM_POSITIONS_LIST:
			employee_list_at_level = self.levels_to_employees.get(level)
			if employee_list_at_level is not None:
				while len(employee_list_at_level) < positions:
					employee_list_at_level.append(Employee(next_gender))
					if next_gender == "female":
						next_gender = "male"
					else: 
						next_gender = "female"
			level += 1

	# Looks at each employee in dictionary and randomly retains employees based on global attrition rate
	def attrit(self):

		for level in range(NUM_LEVELS):
			updated_employee_list = [] #retained employees will be saved here

			employee_list_at_level = self.levels_to_employees.get(level)
			
			for employee in employee_list_at_level:
				if random.randrange(0, 100) > ATTRITION:
					updated_employee_list.append(employee)
			
			self.levels_to_employees[level] = updated_employee_list #saves new list to dictionary
			employee_list_at_level = self.levels_to_employees.get(level)
			

    # Looks at each level, determines the number of promotions, adds and deletes employees
	# to various levels
	# def promote(self):
	# 	current_level = NUM_LEVELS - 1
	# 	while current_level > 0: #2, 1
	# 		candidates = self.levels_to_employees.get(current_level)
	# 		candidates.sort(key=lambda x: x.rating, reverse=True)
 # 			targets = self.levels_to_employees.get(current_level + 1)
 # 			print "candidates", len(candidates)
 # 			# print "next level", NUM_POSITIONS_LIST[level + 1]
 # 			print "targets", len(targets)
	#  		num_promotions = min(len(candidates), NUM_POSITIONS_LIST[current_level + 1] - len(targets))
	#  		# print "+++"
	#  		# print "level", level
	#  		# print "num_promotions", num_promotions
	#  		current_level -= 1

	#  		for i in range(num_promotions + 1):

	#  			promoted = candidates[0]
	#  			targets.append(promoted)
	#  			candidates.remove(promoted)
	 		
	#  		self.levels_to_employees[current_level] = candidates
	#  		# saved_candidates = self.levels_to_employees[level]
	 			
	#  		self.levels_to_employees[current_level + 1] = targets

	def promote(self):
		for level in range(NUM_LEVELS):
			candidates = self.levels_to_employees.get(level)

			capacity = NUM_POSITIONS_LIST[level]
			open_positions = capacity - len(candidates)
			print "level", level
			print open_positions

			candidates.sort(key=lambda x: x.rating, reverse=True)

			targets = self.levels_to_employees.get(1)
			# for num in range(open_positions):
			targets.append(candidates[0])
			targets.append(candidates[1])		
		
			# for num in range(open_positions):
			del candidates[0]
			del candidates[0]


	def run(self):
		for i in range(0, ITERATIONS_PER_SIMULATION):
			self.talent_review()
			self.attrit()
	      	self.promote()
	      	# self.hire()



def summarize(results):
	print("Level   Men          Women")
	print("        avg     %    avg         %")
	print("-----   -----------  -----------")

	for level in range(0, NUM_LEVELS): 
		men_averager = Averager()
		women_averager = Averager()

		for result in results:
			men_averager.add(result.men[level])
			women_averager.add(result.women[level])


	  	total_employees = men_averager.get_total() + women_averager.get_total()
	  	men_avg = men_averager.get_average()
	  	men_percentage = 100 * men_averager.get_total() / total_employees
	  	women_avg = women_averager.get_average()
	  	women_percentage = 100 * women_averager.get_total() / total_employees

	  	summary = "{0:5}{1:5}{2:8} %{3:5}{4:11} %".format(level + 1, men_avg, men_percentage, women_avg, women_percentage)
	  	print summary


def main():
	print("Running {} simulations.".format(NUM_SIMULATIONS))
	print("{0:2}% bias for men".format(PROMOTION_BIAS))
	print("{0:2} promotion cycles".format(ITERATIONS_PER_SIMULATION))
	print("{0:2}% attrition rate".format(ATTRITION))
	print("")

	results = []
	for i in range(0, NUM_SIMULATIONS):
		simulation = Simulation()
  		simulation.run()
  		results.append(simulation.get_result())

	summarize(results)


if __name__ == "__main__": 
	main()


