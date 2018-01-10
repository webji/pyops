#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 12:45:12



import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

import pyops

install_requires = [
    'click>=3.3',
    'unittest2>=0.5.1'
]

setup(
    name='pyops',
    version=pyops.__version__,

    description='IT maintenance and operation libs in Python.',
    long_description=long_description,

    url='https://github.com/webji/pyops',

    author='Will Ji',
    author_email='willji@outlook.com',

    license='Apache License, Version 2.0',

    classifiers=[
        'Programming Language :: Python :: 2.7',

        'License :: OSI Approved :: Apache Software License',

        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='maintencance operations it',

    packages=find_packages(exclude=['data', 'tests*']),

    install_requires=install_requires,

    extras_require={},

    package_data={
        'pyops': [
            'logging.conf',
        ],
    },

    entry_points={
        'console_scripts': [
            'pyops=pyops.run:main'
        ]
    },

    test_suite='tests.all_suite',
)