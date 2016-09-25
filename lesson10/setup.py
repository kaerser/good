#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/9/25 23:56
"""

from distutils.core import setup
from setuptools import find_packages

setup(
	name = 'kaerserdemo',
	version = '1.0.0',
	url = 'http://',
	license= 'Apache',
	author='kaerser',
	author_email='kaermessi@163.com',
	description='This is Test',
	classifiers=['Programming Language:Python'],
	platforms='any',
	packages=find_packages(exclude=[]),
	install_requires=[],
)