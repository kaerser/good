#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/18 18:27
"""

import numpy as np

if __name__ == '__main__':
	user_info = np.loadtxt('./user_message',delimiter='|',dtype=np.string_)
	print user_info