#!/usr/bin/env python
import os, sys

from django.core.management import execute_manager

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

EXTERNAL_APPS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'external_apps'))
sys.path.append(EXTERNAL_APPS
                    )
if __name__ == "__main__":
    execute_manager(settings)
