`cd django\demoproject`

## Virtual Environment

Create Virtual Environment

`python3 -m venv env`

Activate Virtual Environment

`source env/bin/activate`

Deactivate Virtual Environment

`deactivate`

## Django

Create a project

`django-admin startproject myproject`

Create a app

`python manage.py startapp myapp | django-admin startapp myapp`

This command starts Django’s built-in development server on the local machine with IP address 127.0.0.1 and port 8000.

`python manage.py runserver`

Django manages the database operations with the ORM technique. Migration refers to generating a database table whose structure matches the data model declared in the app.

`python manage.py makemigrations`

This command option of manage.py synchronizes the database state with the currently declared models and migrations.

`python manage.py migrate`
