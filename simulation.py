import math
import random
import time

from employee import Employee
from result import Result


class Simulation:

    def __init__(self, num_simulations, attrition, iterations_per_simulation, promotion_bias, 
        num_positions_list, bias_towards_gender):
        self.num_simulations = num_simulations
        self.attrition = attrition
        self.iterations_per_simulation = iterations_per_simulation
        self.promotion_bias = promotion_bias
        self.num_positions_list = num_positions_list
        self.bias_towards_gender = bias_towards_gender
        self.num_levels = len(num_positions_list)

        self.init_employees()
        self.hire()

    def init_employees(self):
        """Build up mapping of level to list of empty array, which will
        eventually be populated with Employees"""

        self.levels_to_employees = {}
        for i in range(0, self.num_levels):
            self.levels_to_employees[i] = []

    def hire(self):
        """Populates levels_to_employees with 50% male/50% female employees"""
        gender = ['male', 'female']
        #randomly assign gender to first employee
        next_gender = random.choice(gender)
        level = 0
        for positions in self.num_positions_list:
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
        """run simulation"""
        for _ in xrange(0, self.iterations_per_simulation):
            self.talent_review()
            self.attrit()
            self.promote()
            self.hire()

    def talent_review(self):
        """Looks at each employee object in dictionary, checks gender and gives
        random performance rating"""
        for employee_list in self.levels_to_employees.values(): 
            for employee in employee_list:
                if employee.gender == self.bias_towards_gender:
                    employee.rating = random.randint(0, 100 + int(self.promotion_bias))
                else:
                    employee.rating = random.randint(0, 100)

    def attrit(self):
        """Looks at each employee in dictionary and randomly retains employees
        based on global attrition rate"""

        for level in range(self.num_levels):
            retained_employees = []
            employee_list_at_level = self.levels_to_employees.get(level)
            num_employees_at_level = len(employee_list_at_level)
            num_employees_to_be_deleted = int(num_employees_at_level * (self.attrition/100.0))
            indexed_employees_to_be_deleted = random.sample(range(num_employees_at_level), num_employees_to_be_deleted)

            for i in range(num_employees_at_level):
                if i not in indexed_employees_to_be_deleted:
                    retained_employees.append(employee_list_at_level[i])
            self.levels_to_employees[level] = retained_employees


    def promote(self):
        """Looks at each level, determines the number of promotions, adds and
        deletes employees to various levels"""
        # start = time.clock()
        for i in range(self.num_levels - 1):
            prev_level = i
            candidates = self.levels_to_employees.get(prev_level)
            new_level = i + 1
            targets = self.levels_to_employees.get(new_level)

            candidates.sort(key=lambda x: x.rating, reverse=True)

            num_candidates = len(candidates)
            open_positions = self.num_positions_list[new_level] - len(targets)
            num_promotions = min(num_candidates, open_positions)
            candidates_to_promote = candidates[:num_promotions]

            self.levels_to_employees[prev_level] = candidates[num_promotions:]
            self.levels_to_employees[new_level] = targets + candidates[:num_promotions]
            candidates = self.levels_to_employees.get(prev_level)

            targets = self.levels_to_employees.get(new_level)
        # print time.clock() - start, "promote method time"

    def get_result(self):
        """Counts number of men and women at each level and saves totals to
        num_men or num_women lists"""
        num_men = [0] * self.num_levels
        num_women = [0] * self.num_levels

        for level in range(self.num_levels):
            employee_list = self.levels_to_employees.get(level)

            for employee in employee_list:
                if employee.gender == "male": 
                    num_men[level] += 1
                else:
                    num_women[level] += 1

        return Result(num_men, num_women)
