#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/22 0:28
"""

from jinja2 import Template

temp = Template('hello {{ name }}')
print temp.render(name = 'world')
