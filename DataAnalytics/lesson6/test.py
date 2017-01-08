#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/06 下午 12:36
"""

from __future__ import division
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4, threshold=500)
pd.options.display.max_rows = 100

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
	y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
	y = y[y.notnull()] #剔除空值
	return lagrange(y.index, list(y))(n) #插值并返回插值结果


if __name__ == "__main__":
	inputfile = './data/catering_sale.xls'
	outputfile = './data/sales.xls'
	data = pd.read_excel(inputfile)
	print data
	data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
	#逐个元素判断是否需要插值
	for i in data.columns:
		for j in range(len(data)):
			if (data[i].isnull())[j]: #如果为空即插值。
				data[i][j] = ployinterp_column(data[i], j)

	data.to_excel(outputfile)


