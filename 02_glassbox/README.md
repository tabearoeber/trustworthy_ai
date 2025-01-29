# Week 02 – Glassbox models


## set up

Before running the notebook, make sure to create a new virtual environment and install the necessary packages:

```
# navigate to parent directory using cd and activate environment
cd ...

# create environment
python3.9 -m venv week2_venv

# activate environment
source week2_venv/bin/activate

# for General Additive Models (GAMs), Explainable Boosting Machine (EBM), and Decision Lists, Rule Generation
pip install numpy scikit-learn==1.1.2 ipykernel interpret statsmodels skope-rules greenlet==1.1.3 gevent==21.8.0 pygam ruleopt

# for Sparse Decision Trees
pip install graphviz cython
git clone https://github.com/ubc-systopia/pydl8.5-lbguess.git
cd pydl8.5-lbguess
python3 setup.py install

# close environment
deactivate
```
