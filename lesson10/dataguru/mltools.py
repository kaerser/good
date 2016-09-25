#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/9/25 23:54
"""

import math

def sigmod(x):
	m = math.e
	n = pow(m, x)
	return n / (n + 1)

if __name__ == '__main__':
	pass