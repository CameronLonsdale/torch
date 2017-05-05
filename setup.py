#!/usr/bin/env python

from setuptools import setup

setup(
    name="torch",
    version='0.1',
    py_modules=['torch'],
    install_requires=[
        'click',
        'lantern'
    ],
    entry_points='''
        [console_scripts]
        torch=torch:cli
    ''',
)
