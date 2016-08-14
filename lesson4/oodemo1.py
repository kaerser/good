#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/14 14:31
"""

# class Dog:
# 	pass
#
# class DogNew(object):
#
# 	def __init__(self):
# 		self.__name = name
#
#
#
# print type(Dog)
# print type(DogNew)
#
#
# wangcai = Dog()
# print wangcai


class Person(object):
	pass

class Chinese(Person):
	nation = 'China'

	def __init__(self,name,age,sex):
		self.name = name
		self._age = age
		self.__sex = sex

	def __str__(self):
		return self.__sex

	def getSex(self):
		return self.__sex

	def setSex(self,sex):
		self.__sex = sex

	@property
	def Age(self):
		return self._age

	@Age.setter
	def Age(self,age):
		self._age = age

	@classmethod
	def getPeople(cls):
		pass

zhangsan = Chinese('zhangsan',20,'m')

print zhangsan.nation
print zhangsan.name
print zhangsan._age
# print zhangsan.__sex
# print zhangsan._Chinese__sex

# print zhangsan.getSex()
# zhangsan.setSex('f')
# print zhangsan.getSex()
# print zhangsan

# print zhangsan
# print dir(zhangsan)

print zhangsan.Age