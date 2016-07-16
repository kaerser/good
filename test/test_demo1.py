#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/16 15:04
"""

import unittest
from lesson1.demo1 import add


class MyTestCase(unittest.TestCase):
	# def test_something(self):
	# 	self.assertEqual(True, False)

	def test_add(self):
		a, b = 3, 4
		c = add(a, b)
		self.assertEqual(c, 7, 'Check Failed!')


if __name__ == '__main__':
	unittest.main()
