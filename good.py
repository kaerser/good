#!/usr/bin/python
# -*-coding:utf-8-*-
'''
@author__ = 'kaerser'
@time:2016/7/16 14:37
'''

# 从文本中读取账户信息
user_message = open('user_message', 'r')
l = user_message.readlines()
dict_user = {}
for i in l:
	m = i.split('|')
	username, passwd, login_num = m[0], m[1], m[2].strip()
	dict1 = {passwd: login_num}
	dict_user[username] = dict1
print dict_user.keys()

# input your message
count = 0
while True:
	login_user = raw_input('Please input your username:')
	# login_passwd=pwd_input('Please input your password:')
	if login_user in dict_user.keys():
		login_passwd = raw_input('Please input your password:')
		# check your password
		if dict_user[login_user].keys()[0] == login_passwd:
			print 'Congratulation! U are login in now!'
			break
		else:
			print 'No,input worry! Pleasr input again!'
			count += 1
			if count > 2:
				print 'Your account is locked!'
				break
	else:
		# notify input again
		print 'No User! Please input again!'
