#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/17 23:48
"""

from MySQLdb import connect

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
	print '你输入的IP有效，请等候查询结果....'

	# 连接数据库
	params = dict(host='localhost', port=3306, user='root', passwd='123456', db='test',use_unicode=True,charset='utf8')
	conn = connect(**params)

	# 创建游标
	cur = conn.cursor()

	# 执行SQL语句，在数据库内实现IP地址的精确查找
	sqltemp = '''
		select country,mobile from iplist where inet_aton(%s) between inet_aton(start_ip) and inet_aton(end_ip)
	'''
	cur.execute(sqltemp,CheckIP)
	for j in cur:
		# print j[0],j[1]
		print '你输入的IP所属国家（地区）为： %s，所属组织为： %s' % (j[0].encode('utf-8'),j[1].encode('utf-8').strip())
	conn.close()