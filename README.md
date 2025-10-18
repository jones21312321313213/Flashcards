inig clone nimo sa repo do these steps:

1)create a virtual environment(.venv):

WINDOWS:
python -m venv .venv

.venv\Scripts\activate

MAC/LINUX:

python3 -m venv .venv

source .venv/bin/activate

2)install dependencies:

pip install -r requirements.txt

3)Create the database ("dbflashcards") in your local workbench and change the settings in flashcards to match your workbench user & pass


4)Then run migrations:

(python/py) manage.py migrate

5) create a super user:

python manage.py createsuperuser

6)Runserver:

python manage.py createsuperuser




