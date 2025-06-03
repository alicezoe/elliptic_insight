# The __init__.py file marks a directory as a Python package and can be used to initialize package-level variables, import submodules, or define the package version.

from os.path import isfile
from os.path import dirname

version_file = '{}/version.txt'.format(dirname(__file__))

if isfile(version_file):
    with open(version_file) as version_file:
        __version__ = version_file.read().strip()
