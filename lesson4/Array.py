#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/14 19:45
"""

import ctypes

class Array :

	def __init__(self,size):
		assert size > 0, "Array size must be > 0"
		self._size = size
		PyArrayType = ctypes.py_object * size
		self._elements = PyArrayType()
		self.clear(None)

	def __len__(self):
		return self._size

	def __getitem__(self, index):
		assert index >= 0 and index < len(self),"Array subscript out of range."
		return self._elements[index]

	def __setitem__(self, index, value):
		assert index >= 0 and index < len(self),"Array subscript out of range."
		self._elements[index] = value

	def clear(self,vlaue):
		for i in range(len(self)):
			self._elements[i] = vlaue

	def __iter__(self):
		return _ArrayIterator(self._elements)

	def __str__(self):
		return str([ element for element in self._elements])

class _ArrayIterator:
	def __init__(self,theArray):
		self._arrayRef = theArray
		self._curNdx = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._curNdx < len(self._arrayRef):
			entry = self._arrayRef[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration

class Vector(Array):
	def __add__(self, other):
		newVector = Vector(len(self))
		if isinstance(other,int):
			for i in range(len(self)):
				newVector._elements[i] = self._elements[i] + other
			return newVector
		elif isinstance(other,Vector) and len(self._elements) == len(other):
			for i in range(len(self)):
				newVector._elements[i] = self._elements[i] + other._elements[i]
			return newVector

	def __mul__(self, other):
		newVector = Vector(len(self))
		if isinstance(other,int):
			for i in range(len(self)):
				newVector._elements[i] = self._elements[i] * other
			return newVector
		elif isinstance(other,Vector) and len(self._elements) == len(other):
			for i in range(len(self)):
				newVector._elements[i] = self._elements[i] * other._elements[i]
			return newVector

	def dot(self,other):
		assert isinstance(other,Vector)
		assert len(self) == len(other)
		sum = 0
		for i in range(len(self)):
			sum += self._elements[i] * other._elements[i]
		return sum


v1 = Vector(4)
v1[0] = 1
v1[1] = 2
v1[2] = 3
v1[3] = 4

x = 10

v2 = Vector(4)
v2[0] = 2
v2[1] = 3
v2[2] = 4
v2[3] = 5

v3 = v1 + x
v4 = v1 * x
v5 = v1 + v2
v6 = v1 * v2
print "数组v1: %s " % v1
print "输入的整形数字: %d " % x
print "数组v2: %s" % v2
print "数组v1与数字相加结果: %s" % v3
print "数组v1与数字相乘结果: %s" % v4
print "数组v1与数组v2相加结果: %s" % v5
print "数组v1与数组v2相乘结果: %s" % v6
print "数组v1与数组v2相乘点数之和: %s" % v1.dot(v2)
