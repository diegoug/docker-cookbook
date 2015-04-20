#!/bin/bash

__install_requirements() {
cd /opt/django/
source bin/activate
cd Django
pip install -r requirements.txt
}

__run_django() {
cd /opt/django/
source bin/activate
cd Django
python manage.py runserver 0.0.0.0:8000
}

# Call all functions
__install_requirements
__run_django
