python -m venv .vemv
.venv\Scripts\activate
pip install django
pip install djangorestframework
pip install django-bootstrap5
pip install django-crispy-forms
python manage.py makemigrations
python manage.py migrate
cd server
python manage.py runserver

