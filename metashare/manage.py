#!/usr/bin/env python
"""
Project: META-SHARE prototype implementation
 Author: Christian Federmann <cfedermann@dfki.de>
"""
# Magic python path, based on http://djangosnippets.org/snippets/281/

from os.path import abspath, dirname, join
import sys
parentdir = dirname(dirname(abspath(__file__)))
# Insert our dependencies:
sys.path.insert(0, join(parentdir, 'lib', 'python2.7', 'site-packages'))
# Insert our parent directory (the one containing the folder metashare/):
sys.path.insert(0, parentdir)


from django.core.management import execute_manager

try:
    import settings # Assumed to be in the same directory.

except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the " \
      "directory containing %r. It appears you've customized things.\n" \
      "You'll have to run django-admin.py, passing it your settings " \
      "module.\n(If the file settings.py does indeed exist, it's causing" \
      " an ImportError somehow, for example if you shouldn't have created a " \
      "custom 'local_settings.py' file.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
