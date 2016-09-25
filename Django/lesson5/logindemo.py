#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/21 14:38
"""

import web

urls = (
    '/login', 'login',
    '/index', 'index',
	'/page1', 'page1',
	'/page2', 'page2',
)

app = web.application(urls,globals())
render = web.template.render('templates/')

# 数据库连接
dblink = web.database(dbn='mysql', host='localhost', user='root', pw='123456', db='test')

class index(object):
	def GET(self):
		return render.index()

class login(object):
	def GET(self):
		return render.login()

class page1(object):
	def GET(self):
		dict1 = {}
		user = web.input().get('username')
		pw = web.input().get('password')
		result = dblink.select('input')
		for i in result:
			dict1[i.get('name')] = i.get('pass')
		print dict1
		if user in dict1.keys() and dict1[user] == pw:
			return '<p>恭喜你，正常登陆系统!</p>'
		else:
			return '<p>你的输入有误</p>'

	def POST(self):
		return self.GET()

class page2(object):
	def GET(self):
		return render.page2


if __name__ == "__main__":
	app.run()