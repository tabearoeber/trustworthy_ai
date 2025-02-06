# Week 01 – Intro

In this week we will solely focus on setting up your machine. You may skip some steps if you have worked with Github, python, etc. before. We'll start with `Git` and `Github`, and then proceed to install `python`, `Anaconda`, and `Gurobi`.

## `Git` and `Github`

:warning: For this course, it is not strictly necessary to install and use `Git` and/or `Github`, however we advise you to do so as this will make it easier for you to access the course material and see changes made by us, such as updates to the tutorial notebooks. :warning:

:arrow_right_hook: If you choose to skip `Github`, you can directly go to [Set up of your machine](https://github.com/tabearoeber/trustworthy_ai/tree/main/01_intro#Set-up-of-your-machine).

`Git` is a free and open source version control system widely used in software development. It allows developers to track changes in their code over time and collaborate seamlessly. Each person has a complete copy ('clone') of the repository where they can work and make changes offline. Changes are registered in `commits`, which can be pushed and merged to a central server. With every commit, a log is created that includes information such as the changes made, who made the changes, some metadata, and a short textual description of the changes. The difference between two commits are called `diffs`. It is also possible to work on the same project in different `branches`, which allows you to experiment on the code before making any definite changes. Branches can later be merged into the `master`.

`Github` is the most widely used user interface to `Git`. Using `Github`, people can work on repositories which are essentially project folders. Repositories can be private or public. Your public repositories can be viewed by anyone. You can create an offline copy of a repository, which we call `cloning` a repository.

If you'd like to know more, I can recommend this [book](https://git-scm.com/book/en/v2).

<p align="center">
   <img src="../img/github-process-english.png" width="700">
</p>
<p align="center">
    <em>Figure: Github workflow, taken from <a href="https://livablesoftware.com/development-process-in-github-basic-infographic/">here</a>.</em>
</p>

### Installing `Git`

**Installing on Mac**: Easiest is to first download and install [Github Desktop](https://desktop.github.com), which provides a nice GUI. Once installed, you can go to `GitHub Desktop > Install Command Line Tool`. 

**Installing on Windows**: First, download and install [Git for Windows](https://gitforwindows.org). Then, download and install [Github Desktop](https://desktop.github.com). 

### `Github` account

Head to [Github](https://github.com) and create an account.


## Set up of your machine 

### installations

***Python*** – 
Make sure to have a recent version of Python installed on your machine. Some of the newer versions may not (yet) be compatible with some of the packges.

***Gurobi*** –
You will need to have Gurobi Optimizer installed on your machine to run some of the methods. They provide a free academic licence. Please see their [website](https://www.gurobi.com/downloads/) for more information and complete instructions for downloading Gurobi Optimizer and activating the licence.
- Create a user account with your **student email**.
- Download a version of Gurobi Optimizer here: https://www.gurobi.com/downloads/gurobi-software/
- While connected to eduroam or having a VPN connection to campus, request a free academic license. The **Academic Named-User License** is a good fit for our course – it is for a single person, for a single machine. Follow the instructions to activate the license.

***Jupyter notebooks*** – 
We'll mainly work in Jupyter notebooks. You could install Anaconda to run Jupyter notebooks (download here: https://www.anaconda.com/download). You may also use another GUI, like VSCode.

### Setting up a virtual environment and getting started

1. Open _Github Desktop_. Go to `File > Clone repository`. In the window that opens, select URL and then paste the URL of this repo into the field. Also choose the local path, i.e. the location where you want to save the repo and all its content. For this, you should choose a directory in your folders where you would usually save any relevant course materials.

   :warning: If you skipped the installation of `Git` and `Github`, instead download this repo by going to `Code > Download ZIP` on the main page of this repo. Unzip the folder and move it to the location you use for this course. Continue with :two:.
   
   :warning: Any time you see a command like `git clone ...`, instead go to the repo on Github and download the repo like above.

3. Open the terminal (on Mac) or the command line tool (Windows). 

- Navigate to the folder with the repo by typing `cd directory_name`. The directory name should end with `../trustworthy_ai`
- Then, copy/paste and run each of the commands below in the terminal/command line tool:

**MacOS**
```
cd <path_to_repo>

python3.9 -m venv test_venv

source test_venv/bin/activate

pip install numpy==1.24 scikit-learn==1.1.2 pandas ipykernel

python -m ipykernel install --user --name=test_venv

deactivate
```

**Windows (cmd)**
```
cd <path_to_repo>

python3.9 -m venv test_venv

test_venv\Scripts\activate

pip install numpy==1.24 scikit-learn==1.1.2 pandas ipykernel

python -m ipykernel install --user --name=test_venv

deactivate
```


You can also create a virtual environment using `conda` (you need to have Anaconda installed for this):
```
cd <path_to_repo>

conda create --name test_venv python=3.10 # specifcy python version you want

conda activate test_venv

conda install jupyter ipykernel # you can also use pip install for packages that are not availble via conda

python -m ipykernel install --user --name=test_venv

conda deactivate
```

## Getting started (finally)

Open `Anaconda` and launch `Jupyter Notebook` from there. Your browser will open and you'll be able to browse your files. Navigate to the folder with the course material. To create a new notebook, on the rop right, click on `New > trustworthy_ai_venv`. A new notebook will open in a new tab. 

Ideally, you create a new notebook for each tutorial and each assignment or create a copy of the files in the repo. This way, there won't be any clashes in case we update the notebooks later on.

---

## Data

We will be using several datasets throughout the tutorials and assignments. For each dataset, we did some pre-processing as you can see in the notebooks in this directory. After setting up your machine, you may run either of the notebooks to check if your environment works fine.


