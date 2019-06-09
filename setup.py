#!/usr/bin/env python

from setuptools import setup

setup(
    name="torch-crypto",
    version='0.1.1',
    description="Command-line Cryptanalysis",
    author='Cameron Lonsdale',
    author_email='cameron.lonsdale@gmail.com',
    url='https://github.com/CameronLonsdale/torch',
    license='MIT',
    install_requires=[
        'click>=7.0',
        'lantern>=0.1.2'
    ],
    scripts=['torch.py'],
    entry_points={
        'console_scripts': ['torch=torch:cli']
    }
)
