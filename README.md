# quizzer

## Requirements
 - Python 3.11

## Local development
 1. Clone the repository.
 ```
    git clone git@github.com:lambton-2024w/quizzer.git
 ```
 2. Create a virtual environment
 ```
 py -3.11 -m venv venv
 ```
 3. Activate the virtuual environment.
 ```
 venv\scripts\activate
 ```
 3. Install requirements.
 ```
 pip install -r requirements.txt
 ```
 4. Running the dev server
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




