#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/31 2:09
"""

from mysort import mysort

if __name__ == "__main__":
	# 读取本地文件中的英文内容
	con = open('word.txt','r')
	f = con.read()
	list1 = []
	set1 = set()
	dict1 = {}
	# print f.split(' ')
	for i in f.split(' '):
		# 初始化文本文件
		# print i.strip(',').strip('.').strip('(').strip(')').strip(':')
		word = i.strip(',').strip('.').strip('(').strip(')').strip(':')
		# 获取所有单词列表和单词
		list1.append(word)
		set1.add(word)
	for l in set1:
		n = 0
		for m in list1:
			if l == m:
				n+=1
		dict1[l] = n
	# print dict1.values()
	set2 = set(mysort(dict1.values()))
	print set2
	# print mysort(dict1.values())[-1]
	for k,v in dict1.items():
		if v == mysort(dict1.values())[-1]:
			print "出现次数最多的单词为："+k
			print "出现的次数为："+str(v)
		# set2 : set([1, 2, 3, 4, 7])
		# for t in set2:
		# 	if v == t:
		# 		print "单词 '"+k+"' 出现的次数为："+str(v)

