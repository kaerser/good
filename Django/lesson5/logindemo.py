#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/21 14:38
"""

import web
from web import form

urls = (
	'/login', 'login',
	'/index', 'index',
    '/(test1|test2)', 'test',
)

app = web.application(urls, globals())
# render = web.template.render('templates/')


class index(object):
	def GET(self):
		name = 'World'
		return 'Hello %s' % name
		# return render.index(name)
		# return render.login()


class login(object):
	def GET(self, name):
		name = 'login'
		return 'Hello %s' % name

	def POST(self, name):
		return 'This is POST!'

class test(object):
	def GET(self, name):
		pars = web.input()
		print pars
		return 'This is TEST Page!'

if __name__ == "__main__":
	app.run()