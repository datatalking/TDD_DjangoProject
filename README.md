
[![Python Support](https://img.shields.io/pypi/pyversions/cfg_load.svg)](https://pypi.org/project/cfg_load/)
[![Documentation Status](https://readthedocs.org/projects/cfg_load/badge/?version=latest)](http://cfg-load.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.org/MartinThoma/cfg_load.svg?branch=master)](https://travis-ci.org/MartinThoma/cfg_load)
[![Coverage Status](https://coveralls.io/repos/github/MartinThoma/cfg_load/badge.svg?branch=master)](https://coveralls.io/github/MartinThoma/cfg_load?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

##### Thanks to https://github.com/MartinThoma/cfg_load best practices
* The recommended way to run TDD_DjangoProject is run the 'scrapescript.py' which is inside the /scraper folder
# SOURCE Test-Driven Development with Django by Packt Publishing Kevin Harvey

## Installation

- Clone ``https://github.com/datatalking/TDD_DjangoProject.git``
- Open cloned directory.
- Run ``python manage.py migrate``
- Run ``python manage.py collectstatic``
- Restart your application server ``python manage.py runserver``

#### Upgrade
- Run `pip install django-admin-interface --upgrade`
- Run ``python manage.py migrate`` *(add* ``--fake-initial`` *if you are upgrading from 0.1.0 version)*
- Run ``python manage.py collectstatic --clear``
- Restart your application server

## Usage

`TDD_DjangoProject` is intended to be used as a kata or practice, as example for TDD Django Devops


## Features

* a functional TDD test suite to maintain existing functionality while refactoring to keep our code tidy and maintainable

Not there now, but planned fo the future:

* TODO PATHing setup, location preferences etc.
* TODO Update script for jupyternotebook, python3 and colab imports due to deprications since 2018 when first written
* FIXME update TDD for functional tests specific to my django, now its just general
* TODO add unit tests
* TODO add integraiton tests for SQL



## In Development

* Add coverage tests
  Check tests with `tox`.
