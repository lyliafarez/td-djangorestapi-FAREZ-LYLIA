# td-djangorestapi-FAREZ-LYLIA

# directory
cd td-djangorestapi-FAREZ-LYLIA
# creating my virtual env
python -m venv myenv
myenv\Scripts\activate

# directory
cd research_management
# Django installation inside env
pip install django djangorestframework
pip install django-filter
pip install drf-yasg
pip install --upgrade setuptools


# launch migrations
python manage.py makemigrations research
python manage.py migrate

# lancer l'application
python manage.py runserver                           





