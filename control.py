from flask import Flask, render_template, request
import json

from simulation import Simulation

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    gender = "men"
    bias = "10"
    control = Control(gender, bias)
    control.run_simulations()
    results = control.fetch_results()
    results=json.dumps(results)
    return render_template("index.html", results=results, gender=gender, bias=bias)

@app.route('/bias', methods=['POST'])
def fetch_bias_amount():
    bias = request.form.getlist('bias')[0]
    gender = request.form.getlist('gender')[0]

    control = Control(gender, bias)
    control.run_simulations()
    results = control.fetch_results()
    results=json.dumps(results)

    return results

class Control:
    """Runs bias simulations based on "Male-Female Differences: A Computer
    Simulation" from the Feb, 1996 issue of American Psychologist.
    http://www.ruf.rice.edu/~lane/papers/male_female.pdf"""

    def __init__(self, bias_towards_gender, promotion_bias):
        self.bias_towards_gender = bias_towards_gender
        self.promotion_bias = int(promotion_bias)
        self.num_simulations = 50
        self.attrition = 15
        self.iterations_per_simulation = 15
        self.num_positions_list = [500, 350, 200, 150, 100, 75, 40, 10]
        self.num_levels = len(self.num_positions_list)

    def run_simulations(self):
        """Run NUM_SIMULATIONS simulations"""
        self.results = []
        append = self.results.append
        for _ in xrange(self.num_simulations):
            simulation = Simulation(self.num_simulations, self.attrition, self.iterations_per_simulation, 
                self.promotion_bias, self.num_positions_list, self.bias_towards_gender)
            simulation.run()
            append(simulation.get_result())

    def fetch_results(self):
        men_data = []
        women_data = []
        # Setting append constructs here, saves compute time in loop
        men_append = men_data.append 
        women_append = women_data.append


        for level in range(0, self.num_levels):
            men_total = 0
            women_total = 0
            for result in self.results:
                men_total += result.men[level]
                women_total += result.women[level]

            total_employees = men_total + women_total
            men_percentage = 100 * men_total / total_employees
            women_percentage = 100 * women_total / total_employees

            men_append(men_percentage)
            women_append(women_percentage)
        print "men", men_data
        print "women", women_data
        return [men_data, women_data]

    def print_summary(self):
        """Print summary"""
        print("Level\tMen\t\t\tWomen")
        print("\tpercent\t%\tpercent\\t%")
        print("-----\t-----------------\t-----------------")

        men_data = []
        women_data = []
        # Setting append constructs here, saves compute time in loop
        men_append = men_data.append 
        women_append = women_data.append


        for level in range(0, self.num_levels):
            men_total = 0
            women_total = 0
            for result in self.results:
                men_total += result.men[level]
                women_total += result.women[level]

            total_employees = men_total + women_total
            men_percentage = 100 * men_total / total_employees
            women_percentage = 100 * women_total / total_employees

            men_append(men_percentage)
            women_append(women_percentage)

            summary = "%d\t%.2f\t%.2f" %(level + 1, men_percentage, women_percentage)
            print summary



if __name__ == "__main__": 
    app.run()
    control = Control('male', 10)
    control.run_simulations()
    results = control.fetch_results()
    summary = control.print_summary()
    # summary = control.print_summary()