#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/17 21:37
"""

def checknum():
	input_num = raw_input("请输入你需要的数字序列（以空格隔开）:")
	list1 = []
	for i in input_num.split(' '):
		l = int(i)
		list1.append(l)
	list1.sort()
	print "你所输入的序列中最大的数为：%d " % list1[len(list1)-1]
	print "你所输入的序列中最小的数为：%d " % list1[0]

def checkstr():
	input_str = raw_input("请输入你需要的字符串参数（以空格隔开）：")
	dict1 = {}
	list1 = []
	for i in input_str.split(' '):
		str_len = len(i)
		dict1[str_len] = i
		list1.append(str_len)
	list1.sort()
	print dict1
	print "你所输入的字符串参数中，长度最长的为：%s " % dict1[list1[len(list1)-1]]
	print "你所输入的字符串参数中，长度最短的为：%s " % dict1[list1[0]]

if __name__ == "__main__":
	checkstr()