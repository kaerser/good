#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/21 14:38
"""

import web
# from web import form

urls = (
    '/login' 'login',
    '/index', 'index',
)

app = web.application(urls,globals())
render = web.template.render('templates/')

class index(object):
	def GET(self):
		# name = 'World'
		# return render.index(name)
		return render.login()

class login(object):
	def GET(self):
		return render.login()


if __name__ == "__main__":
	app.run()