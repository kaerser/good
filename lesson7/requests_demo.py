#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/30/2016 01:21 PM
"""

import requests

url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
response = requests.get(url)
print response.status_code
# print response.text
# image_url = 'https://img3.doubanio.com/view/movie_poster_cover/mpst/public/p2375019545.jpg'
# response = requests.get(image_url)
# f = open(image_url.split('/')[-1],'wb')
# f.write(response.content)
# f.close()
