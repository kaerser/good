#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/6 21:38
"""
import numpy
from datetime import datetime


def pythonsum(n):
	a = range(n)
	b = range(n)
	c = []
	for i in range(len(a)):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i] + b[i])
	return c


def numpysum(n):
	a = numpy.arange(n) ** 2
	b = numpy.arange(n) ** 3
	return a + b


if __name__ == '__main__':
	size = 1000
	# 测试python运行速率
	start1 = datetime.now()
	c1 = pythonsum(size)
	finish_time1 = datetime.now() - start1
	print "Python运行最后的两个元素为：", c1[-2:]
	print "Python运行的总时间为", finish_time1.microseconds

	# 测试numpy运行速率
	start2 = datetime.now()
	c2 = numpysum(size)
	finish_time2 = datetime.now() - start2
	print "Numpy运行最后的两个元素为：", c2[-2:]
	print "Numpy运行的总时间为", finish_time2.microseconds
