#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/31 0:39
"""

import unittest
from lesson2.mysort import mysort

class MyTestCase(unittest.TestCase):
	def test_something(self):
		y = mysort([5,4,3,2,1])
		self.assertEqual(y,[1,2,3,4,5],"Check Failed!")


if __name__ == '__main__':
	unittest.main()
