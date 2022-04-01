# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dbutilsmock',
    version='1.0.0',
    description='Mock to use for Databricks Utils (dbutils) whenever it is not installed, e.g. on you local machine',
    long_description=readme,
    author='Julian Gimbel',
    url='https://github.com/jugi92/dbutilsMock',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)