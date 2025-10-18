inig clone nimo sa repo do these steps:


Creating a virtual environment

windows:

python -m venv .venv
.\.venv\Scripts\activate

mac/linux:

python3 -m venv .venv
source .venv/bin/activate

Then install dependencies:
pip install -r requirements.txt

Then migrate:
python manage.py migrate


make sure to create dbflashcards in your local workbench
