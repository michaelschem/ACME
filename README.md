# Sure ACME

This is an application bilt for SURE to show backend skills in Django.

## How to use this API

## How to run test suite

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