{{ app_name }}
=====================================================================

To install::

    pip install https://github.com/{{ gituser }}/django-{{ app_name }}.git

Then add ``{{ app_name }}`` to your installed apps. ::

    INSTALLED_APPS = (
        ...
        '{{ app_name }}',
        ...
    )

