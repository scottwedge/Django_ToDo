# [Django ToDo](https://ddeveloper72-django-todo.herokuapp.com/)
## An introduction to Django...
## The Mini-Walk Through Tutorial
#### *A part of Full Stack Development*


Welcome to my Django introduction tutorial on VSCode and the Cloud9 IDE!  

[Code Institute](https://courses.codeinstitute.net/) tutorial was all about.

This tutorial focused on creating a Django mini app which at its heart, lets a user 
perform CRUD operations on a simple local sqlite3 database for development and a postgresql
The database is hosted on [Heroku](https://heroku.com/)

Remember, CRUD -> ```Create, Read, Update, Delete```

The Learning Outcomes Are:

1 Learning about the MVT (Model View Template)

   * The Template being the HTML or the presentation layer, 
   * The View layer contains the logic, that the end user will be interacting with.
    
2 Getting data through different models

   * manipulation of data in the view,
   * presenting the data to the user,
   * taking data from the html, passing it to the view and adding to the database.


3 Perform CRUD operations with the data

   * connect using a driver via the standard postgresql URI

4 Using Django's built in test facility

   * Testing app.py
    * Testing models.py
    * Testing views.py
    * Testing forms.py
    
5 Setting up the environmental variables on VSCode and in Cloud 9

    * Configuring Cloud 9
    * Configuring of VSCode - Credit to @Miro for your help

### .vscode settings.json

```javascript
"terminal.integrated.env.windows": {
    "DEVELOPMENT": "true",
    "SECRET_KEY": "My_Secret_Key",
    "DATABASE_URL": "",
    "ADMIN": "admin pass",
    "DJANGO_SETTINGS_MODULE": "django_todo.settings",
    }

```
    * keeping secret keys secret

```python
SECRET_KEY = os.environ.get('SECRET_KEY')


Django settings.py

```python
    if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False
```

[Database](https://docs.djangoproject.com/en/1.11/ref/settings/#databases)

```python
if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
```

6 Deploying our Django app to Heroku [Django ToDo](https://ddeveloper72-django-todo.herokuapp.com/)

    * installing gunicorn and psycopg2, for running our service and to connect to PostgreSQL database