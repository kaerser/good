#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:2016/9/13 15:27
"""

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()