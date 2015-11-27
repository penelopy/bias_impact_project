from numpy import random

from employee import Employee
from result import Result


class Simulation:

    def __init__(self, num_simulations, attrition, iterations_per_simulation, promotion_bias, 
        num_positions_at_level, bias_favors_this_gender):
        self.num_simulations = num_simulations
        self.attrition = attrition
        self.iterations_per_simulation = iterations_per_simulation
        self.promotion_bias = promotion_bias
        self.num_positions_at_level = num_positions_at_level
        self.bias_favors_this_gender = bias_favors_this_gender
        self.num_employee_levels = len(num_positions_at_level)

        self.init_employees()
        self.hire()

    def init_employees(self):
        """Build up mapping of levels with an empty array, which will
        eventually be populated with Employees"""

        self.levels_to_employees = {}
        for i in range(0, self.num_employee_levels):
            self.levels_to_employees[i] = []

    def hire(self):
        """Populates levels_to_employees with 50% male/50% female employees"""
        gender = ['male', 'female']
        #randomly assign gender to first employee
        next_gender = random.choice(gender)
        level = 0
        for positions in self.num_positions_at_level:
            employee_list_at_level = self.levels_to_employees.get(level)
            append = employee_list_at_level.append
            if employee_list_at_level is not None:
                while len(employee_list_at_level) < positions:
                    append(Employee(next_gender))
                    if next_gender == "female":
                        next_gender = "male"
                    else: 
                        next_gender = "female"
            level += 1

    def run(self):
        """Run simulation"""
        for _ in xrange(0, self.iterations_per_simulation):
            self.attrit()       
            self.talent_review()

            self.promote()
            self.hire()

    def talent_review(self):
        """Looks at each employee object in dictionary, checks gender and gives
        random performance rating"""
        bias = 100 + self.promotion_bias
        for employee_list in self.levels_to_employees.values(): 
            for employee in employee_list:
                if employee.gender == self.bias_favors_this_gender:
                    employee.rating = random.randint(0, bias)
                else:
                    employee.rating = random.randint(0, 100)


    def attrit(self):
        """Looks at each employee in dictionary and removes the lowest ranking 
           employees in each level"""

        for level in range(self.num_employee_levels):
            employee_list_at_level = self.levels_to_employees.get(level)
            num_employees_at_level = len(employee_list_at_level)
            num_employees_to_retain = int(num_employees_at_level * ((100 - self.attrition)/100.0))
            employee_list_at_level.sort(key=lambda x: x.rating)
            attrition = num_employees_at_level - num_employees_to_retain

            self.levels_to_employees[level] = employee_list_at_level[attrition:]


    # def attrit(self):
    #     """Looks at each employee in dictionary and randomly retains employees
    #     based on global attrition rate"""

    #     for level in range(self.num_employee_levels):
    #         employee_list_at_level = self.levels_to_employees.get(level)
    #         num_employees_at_level = len(employee_list_at_level)
    #         num_employees_to_retain = int(num_employees_at_level * ((100 - self.attrition)/100.0))
    #         indices_to_retain = random.choice(range(num_employees_at_level), num_employees_to_retain)
    #         retained_employees = []
    #         for i in indices_to_retain: 
    #             retained_employees.append(employee_list_at_level[i])

    #         self.levels_to_employees[level] = retained_employees

    def promote(self):
        """Starts at highest level and checks for open positions, then removes the top
        employees from the level below to fill the open positions. Continues this process through 
        each lower level. Only the entry level will have open positions at the end of this method."""
        for i in range(self.num_employee_levels - 1, 0, -1):
            promote_to_level = i
            promote_from_level = i - 1

            promote_from_employees = self.levels_to_employees.get(promote_from_level)

            promote_to_employees = self.levels_to_employees.get(promote_to_level)

            promote_from_employees.sort(key=lambda x: x.rating, reverse=True)

            num_candidates = len(promote_from_employees)
            total_positions = self.num_positions_at_level[promote_to_level]
            filled_positions = len(promote_to_employees)
            open_positions = total_positions - filled_positions
            num_promotions = min(num_candidates, open_positions)
            candidates_to_promote = promote_from_employees[:num_promotions]
            # Saves revised data back to the dictionary
            self.levels_to_employees[promote_from_level] = promote_from_employees[num_promotions:]
            self.levels_to_employees[promote_to_level] = promote_to_employees + candidates_to_promote

    def get_result(self):
        """Counts number of men and women at each level and saves totals to
        the corresponding list."""
        total_men_at_level = [0] * self.num_employee_levels
        total_women_at_level = [0] * self.num_employee_levels

        for level in range(self.num_employee_levels):
            employee_list = self.levels_to_employees.get(level)

            for employee in employee_list:
                if employee.gender == "male": 
                    total_men_at_level[level] += 1
                else:
                    total_women_at_level[level] += 1

        return Result(total_men_at_level, total_women_at_level)
