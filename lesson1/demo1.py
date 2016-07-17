#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/16 14:32
"""
import math


def add(x, y):
	return x + y


def sigmod(x):
	m = math.e
	n = pow(m, x)
	return n / (n + 1)


if __name__ == '__main__':
	t = float(raw_input("请输入要计算的数值："))
	print sigmod(t)
