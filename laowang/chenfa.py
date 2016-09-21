#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/21 9:20
"""


def multiplication(a):
	x = 1
	while x < (a + 1):
		for i in range(x):
			i += 1
			print '%d*%d=%d' % (x, i, x * i),
		x += 1
		print


if __name__ == "__main__":
	multiplication(10)