#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/15 下午 04:28
"""

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
	file_path = './data/tips.csv'
	df = pd.read_csv(file_path)
	# 统计不同time的tip的均值，方差
	fun = ['mean','var']
	print df['tip'].groupby(df['time']).agg(fun)

	# 将total_bill和tip根据不同的sex进行标准化(原数据减去均值的结果除以标准差)
	def fun1(arr):
		return (arr-arr.mean())/arr.std()
	print df.groupby('sex')[['total_bill','tip']].apply(fun1)


	# 计算吸烟者和非吸烟者的小费比例值均值的差值
	df['tip_pct'] = df['tip'] / df['total_bill']
	tip_pct_smoker = df['tip_pct'].groupby(df['smoker']).mean()
	print '吸烟者和非吸烟者的小费比例值均值的差值为%f' % (tip_pct_smoker['Yes'] - tip_pct_smoker['No'])

	# 对sex与size聚合，统计不同分组的小费比例的标准差、均值，将该标准差与均值添加到原数据中
	grouped1 = df.groupby(['sex','size'])
	fun2 = ['std','mean']
	print grouped1['tip_pct'].agg(fun2)

	# 对time和size聚合，画出total_bill的饼图
	def fun3(arr):
		return arr[:arr.count()]
	grouped2 = df.groupby(['time','size'])
	print grouped2['total_bill'].apply(fun3)


