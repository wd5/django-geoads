# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import setup, find_packages
import re
import os

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='django-geoads',
    version='0.0.2',
    description='Django app for geolocated ads',
    long_description=readme,
    author='Samuel Goldszmidt',
    author_email='samuel.goldszmidt@gmail.com',
    url='https://github.com/ouhouhsami/django-geoads',
    license=license,
    packages=find_packages(exclude=('docs', )),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        #'Django==1.3',
        #'psycopg2==2.4.1',  # Python-PostgreSQL Database Adapter
        # 2.4.1 version for this reasaon:
        # http://obroll.com/solve-psycopg2-programmingerror-autocommit-in-django-1-3-1-postgresql-run-test/
        #'django-moderation'
    ],
    classifiers=['Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities'],
    test_suite='example_project.runtests.runtests',
)
