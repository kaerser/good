#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/9/13 23:42
"""

import ConfigParser

if __name__ == '__main__':
	cf = ConfigParser.ConfigParser()
	cf.read('test.ini')

	s = cf.sections()
	for i in s:
		print cf.items(i)