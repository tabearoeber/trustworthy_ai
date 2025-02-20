# Week 03 – Unboxing Methods

In this notebook we'll be training a black-box model to the dataset which we will then explain using different post-hoc explanation methods.

Make sure to install the required packages. You can use the lines below to set up your environment. You may also use the environment of last week and install the missing packages in there.
 
```
# navigate to parent directory using cd and activate environment
cd <path-to-week3>

# create and activate new environment
# on Mac
python3.11 -m venv week3_venv
source week3_venv/bin/activate

# on Windows
python3.11 -m venv week3_venv
#or 
py -3.11 -m venv week3_venv
week3_venv\Scripts\activate

# install packages
pip install lime shap torch grad-cam

# install jupyter kernel make environment available as kernel 
pip install ipykernel
python -m ipykernel install --user --name=week3_venv

# close environment
deactivate
```
