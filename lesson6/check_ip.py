#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/23/2016 04:40 PM
"""

from pymongo import MongoClient
from mongo_ip_list import ip2long
import json
from bson import json_util

if __name__ == '__main__':
	# 输入需要查询的ip地址
	print '欢迎进入IP地址查询系统，IP地址类似：XX.XX.XX.XX(101.204.3.27)'
	CheckIP = raw_input('请输入你需要查询的IP地址： ')
	m = CheckIP.strip().split('.')

	# 对用户输入的IP地址进行校对
	for i in m:
		# 校对不成功，程序直接退出
		if int(i) < 0 or int(i) > 255:
			print '你所输入的IP地址无效，请输入0-255内的值！！'
			quit()
		else:
			pass
	n = ip2long(CheckIP)
	print '你输入的IP有效，请等候查询结果....'

	# 简历数据库连接
	conn = MongoClient('20.26.3.84')
	db = conn.mydb
	users = db.ips

	# MongoDB中查询IP地址段
	cur = users.find({'Start_IP': {'$lte': n}, 'End_IP': {'$gte': n}},{'_id':0})

	for user in cur:
		t = json.dumps(user, indent=4, default=json_util.default)
		s = json.loads(t)
		print '你输入的IP所属国家（地区）为： %s，所属组织为： %s' % (s['Country'].encode('utf-8'),s['ISP'].encode('utf-8').strip())
