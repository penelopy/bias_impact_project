from flask import Flask

from averager import Averager
from simulation import Simulation

app = Flask(__name__)

@app.route('/')
def home_page(): 
    return render_template("index.html")

class Control:
    """Runs bias simulations based on "Male-Female Differences: A Computer
    Simulation" from the Feb, 1996 issue of American Psychologist.
    http://www.ruf.rice.edu/~lane/papers/male_female.pdf"""

    def __init__(self, bias_towards_gender, promotion_bias = 1):
        self.bias_towards_gender = bias_towards_gender
        self.promotion_bias = promotion_bias
        self.num_simulations = 100
        self.attrition = 15
        self.iterations_per_simulation = 12
        self.num_positions_list = [500, 350, 200, 150, 100, 75, 40, 10]
        self.num_levels = len(self.num_positions_list)

    def run_simulations(self):
        """Run NUM_SIMULATIONS simulations"""
        self.results = []
        for i in range(self.num_simulations):
            simulation = Simulation(self.num_simulations, self.attrition, self.iterations_per_simulation, 
                self.promotion_bias, self.num_positions_list, self.bias_towards_gender)
            simulation.run()
            self.results.append(simulation.get_result())

    def print_header(self):
        """print header with var info"""
        print("Running {} simulations.".format(self.num_simulations))
        print("{0:2}% bias for {1}".format(self.promotion_bias, self.bias_towards_gender))
        print("{0:2} promotion cycles".format(self.iterations_per_simulation))
        print("{0:2}% attrition rate".format(self.attrition))
        print

    def print_summary(self):
        """Print summary"""
        print("Level\tMen\t\t\tWomen")
        print("\tavg\tmedian\t%\tavg\tmedian\t%")
        print("-----\t-----------------\t-----------------")

        for level in range(0, self.num_levels):
            men_averager = Averager()
            women_averager = Averager()
            for result in self.results:
                men_averager.add(result.men[level])
                women_averager.add(result.women[level])

            total_employees = men_averager.get_total() + women_averager.get_total()
            men_avg = men_averager.get_average()
            men_median = men_averager.get_median()
            men_percentage = 100 * men_averager.get_total() / total_employees
            women_avg = women_averager.get_average()
            women_median = women_averager.get_median()
            women_percentage = 100 * women_averager.get_total() / total_employees

            summary = "%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" %(level + 1, men_avg, men_median, men_percentage, women_avg,
                    women_median, women_percentage)
            print summary


if __name__ == "__main__": 
    app.run()
    for gender in ["male", "female"]:
      control = Control(gender)
      control.print_header()
      control.run_simulations()
      control.print_summary()
