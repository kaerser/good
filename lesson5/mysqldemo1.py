#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/16 0:38
"""

import MySQLdb
# 1.创建连接
parmas = dict(host='localhost',port=3306,user='root',passwd='123456',db='test')
conn = MySQLdb.connect(**parmas)

# 2.创建游标
cur = conn.cursor()

# 3.执行SQL语句
# ddl = """
# 	create table users(id INTEGER ,name VARCHAR (40),address VARCHAR (100))
# """
#
# cur.execute(ddl)
#
# sqltxt = '''
# 	insert INTO users(name,address) VALUES ('zhangsan','hangzhou')
# '''
#
# cur.execute(sqltxt)
# conn.commit()

sqltemp = '''
	insert INTO users(name,address) VALUES(%s,%s)
'''

# u1 = ('lisi','shanghai')
# cur.execute(sqltemp,u1)
# conn.commit()

us = [
	('lisi1','shanghai'),
	('lisi2','shanghai'),
	('lisi3','shanghai'),
	('lisi4','shanghai'),
	('lisi5','shanghai'),
	('lisi6','shanghai'),
]

cur.executemany(sqltemp,us)
conn.commit()

sqltxt = '''
	select * from users
'''
cur.execute(sqltxt)
for i in cur:
	print i

# 4.关闭连接
conn.close()