# quizzer

## Project setup 
 
 1. Make sure python >3.11 is installed.
 2. Create a virtual environment
 ```
 python -m venv venv
 ```
 3. Install requirements.
 ```
 pip install -r requirements.txt
 ```


## Run development server
```
python manage.py runserver
```

## Create and apply migrations
After changing models, we need to create migrations and apply them for them to take effect in our db tables.

Creating migrations:
```
python manage.py makemigrations
```

Apply migrations:
```
python manage.py migrate
```