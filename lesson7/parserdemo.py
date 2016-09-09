#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/31/2016 10:59 PM
"""

from HTMLParser import HTMLParser

html_content = '''<title>这是一个标题</title>'''

class TestParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self._tags = []

	def handle_starttag(self, tag, attrs):
		self._tags.append(tag)

	def handle_data(self, data):
		print '/'.join(self._tags) + '=' + data

	def handle_endtag(self, tag):
		self._tags.pop()


if __name__ == '__main__':
	test = TestParser()
	test.feed(html_content)