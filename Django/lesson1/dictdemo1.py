#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/21 22:19
"""

if __name__ == "__main__":
	dict1 = {1:'v1', 4:'k4', 3:'s3', 2:'b2'}
	dict2 = {}
	for i in dict1.keys():
		dict2[i] = dict1[i]
	print dict2

