#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 12:21
"""

# 读入BHP1.csv，使用适当的方法填补缺失值

# 读入BHP2.xlsx，与BHP1数据集合并为BHP数据集

# 将BHP数据集中的成交量（volume）替换为 high、median、low 三种水平（区间自行定义）

from __future__ import division
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from pandas import Series, DataFrame
import pandas as pd

def ployinterp_column(s, n, k=5):
	y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
	y = y[y.notnull()]
	return lagrange(y.index, list(y))(n)

if __name__ == "__main__":
	bhp1_file = './data/task/BHP1.csv'
	bhp2_file = './data/task/BHP2.xlsx'
	data_bhp1 = pd.read_csv(bhp1_file)
	data_bhp2 = pd.read_excel(bhp2_file)
	print data_bhp1['Open'], data_bhp1.columns
	for i in data_bhp1.columns:
		for j in range(len(data_bhp1)):
			if (data_bhp1[i].isnull())[j]:
				data_bhp1[i][j] = ployinterp_column(data_bhp1[i], j)
	print data_bhp1

	print data_bhp2

	data_bhp = pd.merge(data_bhp1,data_bhp2,how='outer')
	print data_bhp[:10]

	volume = data_bhp['volume']
	id = 0
	for i in volume:
		if i >= 3000000 and i < 4000000:
			data_bhp['volume'][id] = "median"
		elif i >= 4000000 :
			data_bhp['volume'][id] = "high"
		else:
			data_bhp['volume'][id] = "low "
		id+=1
	print data_bhp