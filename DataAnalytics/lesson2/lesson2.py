#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/11/29 10:56
"""

def square(x,y):
	return x**2-y**2

def squares_sum(x):
	if x == 1:
		return 1
	return squares_sum(x-1) + x**2

def check(x):
	if isinstance(x,int):
		if x < 100:
			return '输入正确，输入值为%d' % x
		else:
			return '输入错误，输入值为%d' % x
	else:
		return '输入格式不正确，请重新输入！'

if __name__ == '__main__':
	x = int(raw_input('请输入x值：'))
	y = int(raw_input('请输入y值：'))
	print square(x,y)
	print squares_sum(100)
	print check(x)
