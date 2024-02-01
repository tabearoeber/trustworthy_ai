# course material

This repo contains datasets, jupyter notebooks and other course material relevant for computer labs of the course Trustworthy AI for Business and Society taught as part of the masters Data Science and Business Analytics at the University of Amsterdam. In case of question, please send me an email to [t.e.rober@uva.nl](t.e.rober@uva.nl).

# set up of your machine 

## installations

***Python*** – 
Make sure to have a recent version of Python installed on your machine. Some of the newer versions may not (yet) be compatible with some of the packges. I am using [![Python 3.9.7](https://img.shields.io/badge/Python-3.9.7-green.svg)](https://www.python.org/downloads/release/python-383/)

***Gurobi*** –
You will need to have Gurobi Optimizer installed on your machine to run some of the methods. They provide a free academic licence. Please see their [website](https://www.gurobi.com/downloads/) for more information and complete instructions for downloading Gurobi Optimizer and activating the licence.
- Create a user account with your **student email**.
- Download a version of Gurobi Optimizer here: https://www.gurobi.com/downloads/gurobi-software/
- While connected to eduroam or having a VPN connection to campus, request a free academic license. The Academic Named-User License is a good fit for our course – it is for a single person, for a single machine. Follow the instructions to activate the license.

***Anaconda*** – 
We'll run jupyter notebooks using Anaconda. You can download Anaconda here: https://www.anaconda.com/download 

## virtual environment

```
python3.9 -m venv trustworthy_ai_venv

source trustworthy_ai_venv/bin/activate

pip install gurobipy numpy==1.24 scikit-learn==1.1.2 pandas matplotlib cvxpy ipykernel

pip install cvxpy (you may have to install cmake first)

python -m ipykernel install --user --name=trustworthy_ai_venv

deactivate
```


## structure

For each week, starting week 02, there will be a notebook file with exercises to be done and discussed during the tutorial sessions. The solutions will be made available here after the tutorial. There is also a graded assignment about the material of each week. Again, solutions will be published after the submission deadline.

     .
    ├── datasets/     # datasets used for tutorials and assignments will be made available here
    |   └── ...
    |  
    ├── 01_intro/     # data pre-processing                    
    |   └── ...
    |  
    ├── 02_glassbox/                         
    |   └── ...
    |   
    ├── 03_unboxing/
    |   └── ...
    |   
    ├── 04_other_approaches/
    |   └── ...
    |   
    ├── 05_federated_learning/
    |   └── ...
    |   
    ├── 06_differential_privacy/
    |   └── ...
    |
    └── README.md
  
