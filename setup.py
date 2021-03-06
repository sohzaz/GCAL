# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0.0'

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

setup(
    name='gcal',
    version=version,
    description='Sync Google Calender',
    author='New Indictrans Technologies Pvt Ltd',
    author_email='makarand.b@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
