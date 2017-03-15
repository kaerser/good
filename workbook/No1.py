#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/3/16 0:21
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""

from PIL import Image

img_file = './image/C6blbG6U4AIZN3A.jpg'
img = Image.open(img_file)
print img.show()