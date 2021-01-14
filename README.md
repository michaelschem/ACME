# ACME

This is an application to work with Django.

## How to use this API

Run the startup script.
```shell script
start.sh
```

OR

1) First get your virtual enviornment ready.

```shell script
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Create database.

```shell script
python manage.py makemigrations api
python manage.py migrate
```

3) Create admin user.

```shell script
python manage.py createsuperuser --email admin@schempc.com --username admin
```

Enter a password for your admin account.

4) Load fixtures.

```shell script
python manage.py loaddata api/fixtures/api.yaml
```

5) Start the application with a django server.
```shell script
python manage.py runserver
```
6) Navigate to `http://127.0.0.1:8000/` and make sure server is running.  You should get a welcome message and two
links, one to the admin portal and one to the API.


### API

All functions should be accessible from the API Root as well as forms to submit posts.  Gets can be used by providing 
url parameters in typical fashion.

### Admin

Admin portal allows you to create and modify database.  Make sure to create a user with the create user steps below 
before using this tool otherwise you will not be able to login.


## How to run test suite

```shell script
coverage erase
coverage run ./manage.py test
coverage report -m
coverage html
open htmlcov/index.html

```

or on Mac

```shell script
./test.sh
```

You should get the following.

```shell script
 % ./test.sh
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.........................
----------------------------------------------------------------------
Ran 25 tests in 0.290s

OK
Destroying test database for alias 'default'...
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
api/__init__.py                      0      0   100%
api/admin.py                        12      0   100%
api/apps.py                          3      0   100%
api/migrations/0001_initial.py       7      0   100%
api/migrations/__init__.py           0      0   100%
api/models.py                       77      0   100%
api/serializers.py                  33      0   100%
api/urls.py                          7      0   100%
api/views.py                        25      0   100%
--------------------------------------------------------------
TOTAL                              164      0   100%
```

As well as the HTML page opening for details.

## Manage

### Create Database

```shell script
python manage.py makemigrations api
python manage.py migrate
``` 

### Create Super User

```shell script
python manage.py createsuperuser --email admin@schempc.com --username admin
```

### Create Fixtures

```shell script
python manage.py dumpdata api --format=yaml --indent=4 > api/fixtures/api.yaml
```

### Wipe and Reload Data from Fixture

```shell script
python manage.py flush 
python manage.py loaddata api/fixtures/api.yaml
```

## References

These are references to some of the articles used in the creation of this application. 

[Writing your first Django App](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

[Django Rest Framework](https://stackoverflow.com/questions/22958058/how-to-change-field-name-in-django-rest-framework)

[Model Relations](https://www.django-rest-framework.org/api-guide/relations/)

[Many to One](https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/)

[Models](https://docs.djangoproject.com/en/dev/topics/db/models/)

[Serializers](https://www.django-rest-framework.org/api-guide/serializers/)

[Addign additional fields](https://stackoverflow.com/questions/18396547/django-rest-framework-adding-additional-field-to-modelserializer)

[Testing Tools](https://docs.djangoproject.com/en/3.1/topics/testing/tools/)

[Testing Coverage](https://django-testing-docs.readthedocs.io/en/latest/coverage.html)

[Disable Method in ViewSet](https://stackoverflow.com/questions/23639113/disable-a-method-in-a-viewset-django-rest-framework)

[Unit test serializer Django Rest Framework](https://stackoverflow.com/questions/61350340/unit-test-serializer-django-rest-framework)

[Testing Django Rest](https://www.django-rest-framework.org/api-guide/testing/)
