#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/14 17:21
"""

import itertools

x = [1,2,3,4]

# for p in itertools.permutations(x,3):
# 	print p

# for p in itertools.combinations(x,2):
# 	print p

y = ['a','b','c']

for p in itertools.product(x,y):
	print p