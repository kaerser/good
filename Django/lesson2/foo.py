#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/29/2016 11:55 PM
"""


def foo(a, k=100, *arg1, **arg2):
	print a, k, arg1, arg2


if __name__ == '__main__':
	foo(1)