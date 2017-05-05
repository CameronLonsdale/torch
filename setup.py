#!/usr/bin/env python

from setuptools import setup

setup(
    name="torch-crypto",
    version='0.1',
    install_requires=[
        'click',
        'lantern'
    ],
    scripts=['torch.py'],
    entry_points={
        'console_scripts': ['torch=torch:cli']
    },
)
