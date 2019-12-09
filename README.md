# OpenEats API

[![API Build Status](https://travis-ci.org/open-eats/openeats-api.svg?branch=master)](https://travis-ci.org/open-eats/openeats-api)
[![Coverage Status](https://coveralls.io/repos/github/open-eats/openeats-api/badge.svg)](https://coveralls.io/github/open-eats/openeats-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac4a42717db53286ee8f/maintainability)](https://codeclimate.com/github/open-eats/openeats-api/maintainability)

This is the API that powers OpenEats. It uses Django/Django Rest Framework to power the API. The core responsibilities of the APi are:
- OpenEats REST API
- Django User management with Django REST token auth
- Django Admin panel for creating new users and administration
- Static Media Manangemtn (AKA Recipe Images)

See [the homepage](https://github.com/open-eats/OpenEats) for more information about OpenEats!

# Contributing
Please read the [contribution guidelines](https://github.com/open-eats/openeats-api/blob/master/CONTRIBUTING.md) in order to make the contribution process easy and effective for everyone involved.

# Dev Tips

#### Running tests
To run tests locally:

```bash
cd openeats-web
docker-compose -f test.yml -p test build
docker-compose -f test.yml -p test up -d db
docker-compose -f test.yml -p test run --rm --entrypoint sh api
python manage.py test
```

Note: If this is the first time you are running the tests, give the DB some time to build itself once it's build there is no need to wait again.

#### REST Endpoints
You can access the API roots via there app names:
* Recipes - http://localhost:8000/api/v1/recipe
* Ingredients - http://localhost:8000/api/v1/ingredient/
* Recipe groups - http://localhost:8000/api/v1/recipe_groups/
* News - http://localhost:8000/api/v1/news/
* Lists - http://localhost:8000/api/v1/list/

#### openeats-api setup without docker
- install postgres
- create user and database in postgres - brief linux command help:
```sh
sudo -u postgres createuser --interactive
sudo -u postgres psql
ALTER USER user_name WITH PASSWORD 'new_password';
CREATE DATABASE openeats;
```
- update base/settings.py with DB credentials (step above)
- install python 3 if needed
- install pip if needed
- install virtualenv wrapper (sometimes vewrapper needs some extra tweaking - ref: https://bit.ly/33ZCngc)
```sh
mkvirtualenv openeats
workon openeats
pip install base\requirements.txt
python manage.py createsuperuser --username admin --email xxx@yyy.zzz
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
- api should then be available at: 127.0.0.1:8000/api/v1/recipe/
- admin should then be available at: 127.0.0.1:8000/admin