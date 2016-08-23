#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/23/2016 10:29 AM
"""
from pymongo import MongoClient
import json
from bson import json_util

# 创建数据库连接
conn = MongoClient('20.26.3.84')
db = conn.mydb
users = db.ips

# 对数据库集合进行操作
# u1 = {
# 	'name':'zhang',
#     'mail':['kaer@163.com','123@qq.com','mot@gmail.com']
# }
#
# x = users.insert_one(u1)
#
# print dir(x)
# print x._WriteResult__acknowledged

cur = users.find({
	'Start_IP':{'$lte': 200130027001},'End_IP':{'$gte': 200130027001}
},
{'_id':0}
)

for u in cur:
	# print u
	s = json.dumps(u,indent=4,default=json_util.default)
	t = json.loads(s)
	print "国家： %s" % t['Country'].encode('utf-8')
	print "运营商： %s" % t['ISP'].encode('utf-8')