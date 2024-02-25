#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import abspath, dirname, join

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 1 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 3.7 :: Only
Topic :: Software Development :: Automation Testing
Framework :: Application Framework :: Library
Intended Audience :: DevoTv Product & Tech
'''.strip().splitlines()
with open(join(CURDIR, '../README.md')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='automation',
    version='0.0.7',
    author='rajala srinivasa reddy',
    author_email='rajala.reddy@impressico.com',
    url='WIP',
    keywords='robotframework testing testautomation selenium api',
    license='Apache License 2.0',
    description='Web and API testing library for DevoTV Application using Robot Framework and Python',
    long_description=DESCRIPTION,
    platforms='any',
    zip_safe=True,
    python_requires='>=3.6, <4',
    include_package_data=True,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    packages=find_packages()
)
