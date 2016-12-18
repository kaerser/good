#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/18 17:01
"""

import numpy as np

if __name__ == '__main__':
	arr1 = np.arange(1,5).reshape(2,2)
	arr2 = np.array([[2,5],[1,3]])
	print np.dot(arr1,arr2)
