#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/02/17 上午 10:49
"""

from numpy import *
import pandas as pd
import seaborn as sns
import matplotlib
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

if __name__ == "__main__":
	data1 = pd.read_table('./data/data1.txt',sep='\t')
	x = data1.iloc[:,:6].as_matrix()
	y = data1.iloc[:,6].as_matrix()
	rlr = RLR()
	rlr.fit(x, y)
	# print rlr.get_support()
	print(u'有效特征为：%s' % ','.join(data1.columns[rlr.get_support()]))
	x = data1[data1.columns[rlr.get_support()]].as_matrix()
	lr = LR()
	lr.fit(x, y)
	print(u'模型的平均正确率为：%s' % lr.score(x, y))

