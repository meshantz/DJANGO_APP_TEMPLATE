DJANGO_APP_TEMPLATE
===================

This template provides boilerplate code for starting a django app as a python
distribution.

Usage
-----

The intention is to make use of the django_extensions_ command ``create_app``
like so::

    python manage.py create_app -t /path/to/DJANGO_APP_TEMPLATE/TEMPLATE -p /path/to/distributions {{ app_name }}

Automatic replacement of ``username``, ``email`` and ``gituser`` in
``setup.py`` currently requires my ``create_app_replacement`` branch of
django_extensions in my fork_. Once you've got that, add a dictionary like this
to your ``settings.py``::

    EXTENSIONS_REPLACEMENTS = {
        'username': 'My Name',
        'email': 'my@email.address',
        'gituser': 'mygituser',
    }

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
.. _fork: https://github.com/meshantz/django-extensions/tree/create_app_replacement
