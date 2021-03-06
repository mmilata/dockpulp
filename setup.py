#!/usr/bin/python
import sys
from setuptools import setup, Command

def _simplejson_on_python26():
    if (sys.version_info[0] > 2 or
        (sys.version_info[0] == 2 and
         sys.version_info[1] > 6)):
        return []
    return ['simplejson']

setup(
    name = "dockpulp",
    version = "1.11",
    author = "Jay Greguske",
    author_email = "jgregusk@redhat.com",
    description = ("ReST API Client to Pulp for manipulating docker images"),
    license = "GPLv3",
    url = "https://github.com/release-engineering/dockpulp.git",
    package_dir = {'': '.'},
    packages = ['dockpulp'],
    install_requires = _simplejson_on_python26(),
    scripts = ['bin/dock-pulp.py', 'bin/dock-pulp-bootstrap.py', 'bin/dock-pulp-restore.py'],
    package_data = {'': ['conf/dockpulp.conf']},
)
