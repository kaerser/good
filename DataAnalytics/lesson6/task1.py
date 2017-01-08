#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 01:53
"""

# 读入"肝气郁结证型系数.xls"数据集，将数据集按照等距、小组等量 两种方式 分别分为5组数据，分别计算5组数据的中位数与标准差

from __future__ import division
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from pandas import Series, DataFrame
import pandas as pd

if __name__ == "__main__":
	data_file = './data/task/gqyjzxxs.xls'
	data = pd.read_excel(data_file)
	lab = [0,1,2,3,4]

	# 等距分组数据
	cut1_data = pd.cut(data[u'肝气郁结证型系数'],5,labels=lab)
	print pd.value_counts(cut1_data)
	cut1_all = data[[u'肝气郁结证型系数']].join(pd.get_dummies(cut1_data))
	cut1_data_set = cut1_all[u'肝气郁结证型系数']
	cut1_data_set1 = cut1_data_set[cut1_all[0] == 1]
	cut1_data_set2 = cut1_data_set[cut1_all[1] == 1]
	cut1_data_set3 = cut1_data_set[cut1_all[2] == 1]
	cut1_data_set4 = cut1_data_set[cut1_all[3] == 1]
	cut1_data_set5 = cut1_data_set[cut1_all[4] == 1]
	print '等距分组方式中，第一组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut1_data_set1),cut1_data_set1.median(),cut1_data_set1.std())
	print '等距分组方式中，第二组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut1_data_set2),cut1_data_set2.median(),cut1_data_set2.std())
	print '等距分组方式中，第三组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut1_data_set3),cut1_data_set3.median(),cut1_data_set3.std())
	print '等距分组方式中，第四组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut1_data_set4),cut1_data_set4.median(),cut1_data_set4.std())
	print '等距分组方式中，第五组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut1_data_set5),cut1_data_set5.median(),cut1_data_set5.std())


	# 小组等量分组数据
	cut2_data = pd.qcut(data[u'肝气郁结证型系数'],5,labels=lab)
	print pd.value_counts(cut2_data)
	cut2_all = data[[u'肝气郁结证型系数']].join(pd.get_dummies(cut2_data))
	cut2_data_set = cut2_all[u'肝气郁结证型系数']
	cut2_data_set1 = cut2_data_set[cut2_all[0] == 1]
	cut2_data_set2 = cut2_data_set[cut2_all[1] == 1]
	cut2_data_set3 = cut2_data_set[cut2_all[2] == 1]
	cut2_data_set4 = cut2_data_set[cut2_all[3] == 1]
	cut2_data_set5 = cut2_data_set[cut2_all[4] == 1]
	print '小组等量分组方式中，第一组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut2_data_set1),cut2_data_set1.median(),cut2_data_set1.std())
	print '小组等量分组方式中，第二组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut2_data_set2),cut2_data_set2.median(),cut2_data_set2.std())
	print '小组等量分组方式中，第三组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut2_data_set3),cut2_data_set3.median(),cut2_data_set3.std())
	print '小组等量分组方式中，第四组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut2_data_set4),cut2_data_set4.median(),cut2_data_set4.std())
	print '小组等量分组方式中，第五组数据个数为：%d , 中位数为：%f , 标准差为：%f' % (len(cut2_data_set5),cut2_data_set5.median(),cut2_data_set5.std())


