#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/18 17:10
"""
import numpy as np

if __name__ == '__main__':
	samples = np.random.normal(size=(10,10))
	print '随机生成的100个标准正态数据为：'
	print samples
	print '此数据的均值为：%f，标准差为：%f' % (samples.mean(),samples.std())