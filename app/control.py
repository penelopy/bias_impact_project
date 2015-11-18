from flask import Flask, render_template, request, jsonify
import json

from app import app
from averager import Averager
from simulation import Simulation

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    gender = 'male'
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
        self.promotion_bias = promotion_bias
        self.num_simulations = 20
        self.attrition = 15
        self.iterations_per_simulation = 15
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

    def fetch_results(self):
        men_data = []
        women_data = []

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

            men_data.append(men_percentage)
            women_data.append(women_percentage)

        return [men_data, women_data]


if __name__ == "__main__": 
    app.run()
