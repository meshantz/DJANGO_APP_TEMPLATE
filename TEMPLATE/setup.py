#!/usr/bin/env python
from distutils.core import setup
import os
import {{ app_name }}

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('{{ app_name }}'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        # note this assumes every file you are including is under the
        # {{ app_name }} folder. you will need to modify it if your files are
        # more scattered.
        prefix = dirpath[len('{{ app_name }}/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(name='{{ app_name }}',
      version={{ app_name }}.get_version().replace(' ','-'),
      author='PeaceWorks',
      author_email='info@peaceworks.ca',
      url='http://www.peaceworks.ca/',
      description='django app: {{ app_name }}',
      packages=packages,
      package_dir={'{{ app_name }}': '{{ app_name }}',},
      package_data={'{{ app_name }}': data_files},
      )

