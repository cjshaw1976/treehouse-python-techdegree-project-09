# treehouse-python-techdegree-project-09

This is my submission for review of the Python Techdegree course, Project 9, Improve a Django Project

A requirements.txt is included for creating your own virtual environment.

To install: 
1. Download and extract the zip on your own pc. cd into the created directory.</br>
2. Create and start a virtual environment: </br>
  python3 -m venv myvenv</br>
  source myvenv/bin/activate</br>
3. Install the project requirements</br>
  pip install -r requirements.txt</br>
4. Start the server</br>
  python manage.py runserver 0.0.0.0:8000</br>
You will now be able to open a webpage at 127.0.0.1:8000

To run the tests with coverage:</br>
coverage run --omit=myenve/* manage.py test</br>
coverage report -m</br>
coverage html

For pep8 test</br>
flake8 menu/
