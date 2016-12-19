#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 16/12/19 下午 12:23
"""

import pandas as pd
import numpy as np
import sys
from pandas import Series, DataFrame

if __name__ == "__main__":
	obj = Series([4, 5, 10, -2])
	print obj.values, obj.index, type(obj.values)
	obj2 = Series([10, 4, 9, 10, -4], index=['a', 'b', 'c', 'd', 'e'])
	print obj2
	print obj2[obj2 > 0]
	print obj2 ** 2
	print np.exp(obj2)

	sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
	obj3 = Series(sdata)
	print obj3, obj3.values, obj3.index

	states = ['California', 'Ohio', 'Oregon', 'Texas']
	obj4 = Series(sdata, index=states)
	print obj4

	print obj4.isnull()
	print obj4.notnull()
	print obj3 + obj4

	data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
	        'year': [2000, 2001, 2002, 2001, 2002],
	        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
	frame = DataFrame(data)
	print frame
	print DataFrame(data, columns=['year', 'state', 'pop'])

	frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
	                   index=['one', 'two', 'three', 'four', 'five'])
	print frame2, frame2.columns
	print frame2.year

