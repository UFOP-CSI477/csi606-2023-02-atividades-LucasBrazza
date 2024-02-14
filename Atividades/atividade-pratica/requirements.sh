#!/bin/bash
python3 -m venv myenv
source myenv/bin/activate
pip install django
pip install djangorestframework
pip install django-bootstrap5
pip install django-crispy-forms
cd server
python3 manage.py runserver