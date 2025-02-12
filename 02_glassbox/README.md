# Week 02 – Glassbox models

This week's tutorial is split into two parts that require different set-ups of your virtual environments. These are the instructions for setting up the two virtual environments:

---

## Part I:

#### Step 1: Navigate to this week's directory 
```
cd <path_to_week_2_material>
```

#### Step 2: Create and Activate a virtual environment (Python 3.9)
**MacOS**
```
python3.9 -m venv part1_venv
source part1_venv/bin/activate
```

**Windows (cmd)**
```
python3.9 -m venv part1_venv
part1_venv\Scripts\activate
```

alternatively try: 
```
py -3.9 -m venv part1_venv
part1_venv\Scripts\activate
```

#### Step 3: Install required packages
First, install `ipykernel` to integrate your virtual environment with Jupyter.
```
pip install ipykernel
python -m ipykernel install --user --name=part1_venv
```

Next, install all necessary dependencies from the requirements.txt file.
```
pip install -r requirements.txt
```

#### Step 4: Install `pydl8.5-lbguess`
```
git clone https://github.com/ubc-systopia/pydl8.5-lbguess.git
cd pydl8.5-lbguess
python3 setup.py install
```

--- 

## Part II:

#### Step 1: Navigate to this week's directory 
```
cd <path_to_week_2_material>
```

#### Step 2: Create and Activate a virtual environment (Python 3.9)
**MacOS**
```
python3.11 -m venv part2_venv
source part2_venv/bin/activate
```

**Windows (cmd)**
```
python3.11 -m venv part2_venv
part2_venv\Scripts\activate
```

alternatively try: 
```
py -3.11 -m venv part2_venv
part2_venv\Scripts\activate
```

#### Step 3: Install required packages
First, install `ipykernel` to integrate your virtual environment with Jupyter.
```
pip install ipykernel
python -m ipykernel install --user --name=part2_venv
```

Next, install all necessary packages.
```
pip install ruleopt
```
