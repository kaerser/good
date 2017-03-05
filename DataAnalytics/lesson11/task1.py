#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/2/19 22:48
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

if __name__ == '__main__':
	filename = './data/data1.txt'
	data = pd.read_table(filename)
	x = data.iloc[:,:6].as_matrix()
	y = data.iloc[:,6].as_matrix()
	print x,y
	rlr = RLR()
	rlr.fit(x, y)
	print data[data.columns[rlr.get_support()]].as_matrix()
	# print '有效特征为：%s' % ','.join(data.columns[rlr.get_support()])