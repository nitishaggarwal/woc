# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import woc
version = woc.__version__

setup(
    name='woc',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'woc',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['woc/manage.py'],
)