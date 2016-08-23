#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/23/2016 04:11 PM
"""

from pymongo import MongoClient
import time

# 转换IP为长整型数字
def ip2long(ip):
	list1 = ip.split('.')
	str = ''
	for i in list1:
		i = '0'*(3-len(i))+i
		str += i
	return int(str)

if __name__ == '__main__':
	start_time = time.time()
	# 遍历ips文件
	ip_info = open('2014_global_ips.txt', 'r')
	list1 = []
	title = ['Start_IP', 'End_IP', 'Country', 'ISP']
	for i in ip_info.readlines():
		if len(i.split()) < 4:
			list2 = [ip2long(i.split()[0]), ip2long(i.split()[1]), i.split()[2].decode('gbk'), None]
		else:
			mobile = ' '
			for j in i.split()[3:]:
				mobile = mobile + j.decode('gbk') + ' '
			list2 = [ip2long(i.split()[0]), ip2long(i.split()[1]), i.split()[2].decode('gbk'), mobile]
		dict_info = dict(zip(title, list2))
		list1.append(dict_info)
	# print list1
	ip_info.close()

	# 建立数据库连接
	conn = MongoClient('20.26.3.84')
	db = conn.mydb
	users = db.ips

	# 插入数据
	users.insert_many(list1, ordered=False)
	print "插入全部数据耗时: %d" % (time.time() - start_time)
	conn.close()