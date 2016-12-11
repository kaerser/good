#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 16/12/11 下午 01:20
"""

import numpy as np

if __name__ == "__main__":
	m = np.array([np.arange(2), np.arange(2)])
	print m, m.shape
	print m[0, 0] + m[1, 1]
	shape_set = (3,3)
	t = np.arange(9)
	print t,t.shape
	t.shape = shape_set
	print t,t.shape
	a = np.arange(0,18,2)
	b = np.arange(20,38,2)
	a.shape = shape_set
	b.shape = shape_set
	print a,a.shape
	print b,b.shape
	print np.hstack((a,b)),np.hstack((a,b)).shape
	print np.vstack((a,b)),np.vstack((a,b)).shape
	print np.hsplit(np.hstack((a,b)),3)



