## Gender Bias 
#### and its cumulative effect on careers and organizations

<br>
### View Project: [doesgenderbiasmatter.com(www.doesgenderbiasmatter.com)
<br>


### Getting Started

1. Fork the repository

1. Install virtualenv `$ pip install virtualenvwrapper`

1. Set up virtual env `source /usr/local/bin/virtualenvwrapper.sh`

1. Cd into project folder `cd doesgenderbiasmatter`

1. Make virtualenv  `$ mkvirtualenv venv`

1. Activate virtualenv `$ source venv/bin/activate`

1. Install requirements file into your virtualenv `$ pip install -r requirements.txt`

1. Run server `$ python control.py`

1. View the site on http://localhost:5000

1. Deactivate virtualenv `$ deactivate`


---
### How It Works

#### Overview

The simulation projects gender ratios for a theoretical company with eight hierarchical tiers, starting at entry-level (level 1) and proceeding to executive level (level 8). Gender bias is reflected in performance-review scores, which are used to determine who stays, who leaves, and who gets promoted.

A total of 20 performance-review cycles are generated (representing 2 per year for 10 years). An employee’s performance-review scores are cumulative, and the cumulative totals are used to determine outcomes for each employee.

It is important to note that this simulation reflects the effects of cisgender bias on performance reviews and promotions only. It does not reflect its effects on hiring or firing, nor does it reflect the additional bias that transgender people and people with non-binary gender identities may face in the workplace.

#### Details

Before the simulation begins, there is a 1:1 gender ratio at each level. Performance-review scores are then randomly generated for employees at every level.

The selected type/amount of gender bias is reflected in performance review scores. For example, if a 5% bias in favor of men is selected, the randomly generated performance-review scores for men are padded by 5%.

Once a cycle’s performance-review scores are generated, a 15% turnover rate is applied: 15% employees at each level are randomly selected and removed from the simulation. Next, any positions that have opened up (as a result of turnover) are filled by taking the highest-ranking performers (based on cumulative performance-review scores) from the preceding level.

Note: Because performance-review scores are randomly generated, simulation outcomes may vary.

#### Acknowledgments

This simulation was inspired by ["Male-Female Differences: A Computer Simulation"](http://www.ruf.rice.edu/~lane/papers/male_female.pdf) by Richard F. Martell, David M. Lane, and Cynthia Emrich and [“From bias to exclusion: A multilevel emergent theory of gender segregation in organizations”](http://www.academia.edu/7444928/) by Richard F. Martell, Cynthia Emrich and James Robinson-Cox.


---
### Authors
This project was built by [Penelope Hill](https://github.com/penelopy) during her the final 2 weeks of her Technical Fellowship at Square. Contributions have been made by [Alyssa Pohahau](https://github.com/alyssa), [Wendy Dherin](https://github.com/doubledherin), and [Dina Westland](https://github.com/dina). The idea for this project came from [Eric Burke](https://github.com/eburke). 

---
### License
See [License](LICENSE.txt) file for license rights and limitations (Apache).
