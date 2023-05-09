# Farm Fresh Recipes

## Description:
This is a Website built for anyone between the casual home cook or professional chef to create and store recipes with the world! There are many features including the ability to store and create recipes, add images, create and delete helpful tags, and also delete recipes.

https://user-images.githubusercontent.com/102191748/236646256-0ca5f331-b5c4-4f5c-9350-44cb881d8ee4.mp4

## Project Goals:
Build a functional website for users to create, edit, delete, and view their recipes. During this build, I plan to improve my skills in Python while working with Django Models. I will practice creating class based views vs function based views, and continue to improve my skills working in HTML Templates, and utilize CSS and Bootstrap to style my page, putting an emphasis on design and usability throughout all aspects of this project.

## Start it up:
- Clone this repository into a fresh directory on your computer
- Create a virtual environment. Make sure you are in the freshly cloned folder when you do this!
    - `python -m venv .venv`
- Activate the virtual enviornment.
    - `source .venv/bin/activate`
- Install the required packages.
    - `pip install -r requirements.txt`
- Run migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- Create a super user
    - `python manage.py createsuperuser`
    - follow terminal prompts
- Install recipes
    - `python manage.py loaddata db.json`
- Run server
    - `python manage.py runserver`
- Open your browser to http://localhost:8000
- ENJOY!!!



### Latest Updates:
- Linked the Related Tag Recipe back to it's corresponding detail page

- Created Login Template
- Added Login Path to Project URL's
- Added LoginRequiredMixin to all Create, Update, and Delete Views
- Added Login/Logout Redirect URL's to Project Settings
- Added Logout Path To Project URL's
- Added Login/Logout Links to Base Template Nav
- Added If Statements to Login/Logout/Admin Nav Links

- Import USER_MODEL to Recipe models
- Changed Recipe model Author Field, to Foreign key, to USER_MODEL
- Show Author On Detail Page
- Remove Author Field From Recipe Create View
- Added Form Valid Method to Create Recipe
- Added Author on Recipe Detail Template

### Future Updates:
- Add ability to add Ingriedients lists and steps lists to a recipe directly from the site
- Add custom 404 page
- Add  create user form
- Add user login and log out function
- Add favorite Recipes page only visible to specific user

## Created By:

|Name|Email|GitHub|
|----|-----|-------|
|David "Lewey" Melchor|dlmelchor12@gmail.com|https://github.com/leweymelchor|
