#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/18 17:43
"""

import sys
import numpy as np

if __name__ == '__main__':
	c,v = np.loadtxt('./data.csv',delimiter=',',usecols=(6,7),unpack=True)
	vwap = np.average(c,weights=v)
	print '成交量加权平均价格：%f ' % vwap
	print '算数平均价格： %f ' % c.mean()
	print '时间加权平均价格： %f ' % np.average(c,weights=np.arange(len(c)))
