#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/30/2016 12:00 AM
"""

if __name__ == '__main__':
	# 打开用户信息文件，获取用户列表
	users = open('user.txt', 'r')
	dict1 = {}
	for i in users.readlines():
		dict1[i.split('|')[1]] = i.split('|')[2].strip()
	users.close()

	# 登陆信息平台，手动输入用户信息
	while True:
		username = raw_input('请输入用户名：')
		if username in dict1.keys():
			passwd = raw_input('请输入登录密码：')
			if passwd == dict1[username]:
				print '恭喜你，验证成功！！'
				print '即将为你展示平台所有用户信息'
				print '用户名    密码'
				for k, v in dict1.items():
					print k + '    ' + v
				break
			else:
				print '你输入的密码不正确，请重新输入！！'
				continue
		else:
			print '您输入的用户名不存在，请重新输入用户名！'
			continue
