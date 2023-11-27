# PROJECT MANAGEMENT EMPLOYEE
This is a project to build employee management software, including Department, Employee, Contact models.
- Department: this is a department management model, each department includes many employees
- Employee: this is a model for managing employee
- Contact: this is a model for managing employee contact information, each employee can have many contacts

## Required
- To run the project, you need to install python version 3.11 or higher and install the environments to use python.
- Install virtual environment

## Documents
- Diagrams:
> https://app.diagrams.net/#G1lgDjS34zGeOIvVxiU1fSGROl5Wlx2eQ7

- Analytics documentation
https://docs.google.com/document/d/1G9_XDtGplCehl8lkdVY0qSYwiFesZ7KSunpsyyPerMo/edit

## How to use
### For Linux or MacOS operating systems, replace py with python
1. First, clone this repository on your computer
> git clone https://github.com/hothanhtuan1209/python-training.git

2. Next, move into the directory containing this file:
> cd python-training
> cd django
> cd manager_employees

3. Checkout to branch develop
> git checkout develop

4. You should create virtual environment and install pyenv
- Create virtual environment named 'venv'
> python -m venv venv

- Run virtual environment for Windows
> .\venv\Scripts\activate

- Run virtual environment for MacOS
> source venv/bin/

- Deactivate a virtual environment
> deactivate

- To install all packages and extensions in project
> pip install -r requirements.txt 

5. Create database
> py manage.py makemigrations manager_employees
> py manage.py migrate

6. Running server
>py manage.py runserver

## Contribute
 - If you want to contribute to this project, please create a pull request and clearly describe the changes you propose