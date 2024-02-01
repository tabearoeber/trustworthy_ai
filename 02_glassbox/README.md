# Week 02 – Glassbox models


## set up

Before running the notebook, make sure to install the necessary packages for this week into your virtual environment:

```
# navigate to parent directory using cd and activate environment
cd trustworthy_ai
source trustworthy_ai_venv/bin/activate

# for Rule Generation (RUG)
git clone https://github.com/sibirbil/RuleDiscovery.git

# for General Additive Models (GAMs), Explainable Boosting Machine (EBM), and Decision Lists
pip install interpret statsmodels skope-rules

# for Sparse Decision Trees
pip install graphviz cython
git clone https://github.com/ubc-systopia/pydl8.5-lbguess.git
cd pydl8.5-lbguess
python3 setup.py install

# close environment
deactivate
```
