# Sure ACME

This is an application bilt for SURE to show backend skills in Django.

## How to use this API

1) First start by running the django server.
```shell script
python manage.py runserver
```
2) Navigate to `http://127.0.0.1:8000/` and make sure server is running.  You should get a welcome message and two
links, one to the admin portal and one to the API.

3) From here you can either create your own data using the admin portal or follow steps in the manage section to Create
the database, then  create a super user, and finally load data from the fixtures.

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