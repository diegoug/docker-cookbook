#!/bin/bash

__install_requirements() {
cd /opt/django/
source bin/activate
cd Django
pip install -r requirements.txt
}

__run_supervisor() {
echo "Running the run_supervisor function."
supervisord -n
}

# Call all functions
__install_requirements
__run_supervisor
