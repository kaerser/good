#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/16 1:46
"""

from MySQLdb import connect

if __name__ == '__main__':
	# 遍历ips文件
	ip_info = open('2014_global_ips.txt', 'r')
	list1 = []
	n = 1
	for i in ip_info.readlines():
		if len(i.split()) < 4:
			tuple1 = (n, i.split()[0], i.split()[1], i.split()[2].decode('gbk'),None)
			n += 1
		else:
			mobile = ' '
			for j in i.split()[3:]:
				mobile = mobile+j.decode('gbk')+' '
			tuple1 = (n, i.split()[0], i.split()[1], i.split()[2].decode('gbk'), mobile)
			n += 1
		list1.append(tuple1)
	ip_info.close()
	# print list1

	# 建立数据库连接
	params = dict(host='localhost', port=3306, user='root', passwd='123456', db='test',use_unicode=True,charset='utf8')
	conn = connect(**params)

	# 创建游标
	cur = conn.cursor()

	# # 执行SQL语句
	sqltemp = '''
		insert INTO iplist(id,start_ip,end_ip,country,mobile) VALUES(%s,%s,%s,%s,%s)
	'''
	cur.executemany(sqltemp,list1)
	conn.commit()
	conn.close()
