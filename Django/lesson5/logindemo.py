#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/21 14:38
"""

import web

urls = (
	'/index', 'index',
	'/(test1|test2)', 'test'
	'/(.*)', 'hello',
)
app = web.application(urls, globals())


class index(object):
	def GET(self):
		return 'Yes,This is Index Page!'

	def POST(self):
		pass

	def DEL(self):
		pass

class test(object):
	def GET(self,name):
		return 'I am %s' % name

class hello(object):
	def GET(self,name):
		if not name:
			name = 'World'
		return 'Hello '+name+'!'


if __name__ == "__main__":
	app.run()