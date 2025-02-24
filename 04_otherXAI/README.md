# Week 04 – Counterfactual Explanations & Symbolic Regression


## set up

To be able to run the notebooks in this directory, make sure to install the following packages in your virtual environment. Note that we need Python 3.9 this week.

```
# navigate to week 4 material
cd <./.../04_otherXAI>

git clone https://github.com/tabearoeber/CE-OCL.git

python3.9 -m venv <venv_name>

MacOS: source <venv_name>/bin/activate  
Windows: <venv_name>/Scripts/activate

pip install ipykernel 

python -m ipykernel install --user --name=<venv_name>

pip install -r requirements.txt
```