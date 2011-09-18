DJANGO_APP_TEMPLATE
===================

This template provides boilerplate code for starting a django app as a python
distribution.

Usage
-----

The intention is to make use of the django_extensions_ command ``create_app``
like so::

    python manage.py create_app -t /path/to/DJANGO_APP_TEMPLATE/TEMPLATE -p /path/to/distributions {{ app_name }}

Then, assuming you're using github for version control, you can initialize your
new repository::

    cd /path/to/distributions/{{ app_name }}
    git init
    git commit -a
    git remote add origin git@github.com:<username>/django-{{ app_name }}.git

Once you've got your version control going, you can use pip to install the
distribution as an editable. ::

    pip install -e git@github.com:<username>/django-{{ app_name }}.git#egg=django-{{ app_name }}

.. _django_extensions: https://github.com/django-extensions/django-extensions
