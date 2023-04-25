# FarmFreshRecipes


How to start:

- Clone this repository into a fresh directory on your computer

- Create a virtual environment. Make sure you are in the freshly cloned folder when you do this!

python -m venv .venv

- Once it's active, you can install the packages using pip.

pip install -r requirements.txt

- Run migrations

python manage.py migrate

- Create a super user

python manage.py createsuperuser

- Run server

python manage.py runserver

- Open your browser to http://localhost:8000
