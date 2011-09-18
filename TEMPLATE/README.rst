{{ app_name }}
=====================================================================

To install::

    pip install https://github.com/<username>/django-{{ app_name }}.git

Then add the ``{{ app_name }}`` to your installed apps. ::

    INSTALLED_APPS = (
        ...
        '{{ app_name }}',
        ...
    )

