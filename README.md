inig clone nimo sa repo do these steps:


Creating a virtual environment

WINDOWS:

python -m venv .venv

.venv\Scripts\activate

MAC/LINUX:

python3 -m venv .venv

source .venv/bin/activate


Then install dependencies:

pip install -r requirements.txt


Then change directory:

cd flashcards

Then migrate:

(python/py) manage.py migrate 



make sure to create dbflashcards in your local workbench

