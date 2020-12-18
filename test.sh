coverage erase
coverage run ./manage.py test
coverage report -m
coverage html
open htmlcov/index.html
