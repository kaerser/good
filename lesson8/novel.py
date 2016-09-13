#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:9/3/2016 11:47 AM
"""

from HTMLParser import HTMLParser
from threading import Thread
from Queue import Queue
import os
import time
import sys

import requests

reload(sys)
sys.setdefaultencoding('utf-8')

imgQueue = Queue()

class Novel(object):
	def __init__(self):
		self.attrs = []

	def __str__(self):
		content = []
		for k, v in self.attrs:
			line = '{0} = {1}'.format(k, v)
			content.append(line)
		return '\r\n'.join(content)

	def downloadImg(self, imgpath, headers):
		imgurl = None
		for (k, v) in self.attrs:
			if k == 'novel_img_url':
				imgurl = v
		if imgurl is None:
			return None

		imgname = imgurl.split('/')[-1]
		imglocalpath = os.path.join(imgpath, imgname)
		img = requests.get(imgurl, headers)
		with open(imglocalpath, 'wb') as f:
			f.write(img.content)
		self.attrs.append(('novel_img_localpath', imglocalpath))
		return imglocalpath


def imgDownLoader(imgpath, headers):
	global imgQueue
	while not imgQueue.empty():
		imgurl = imgQueue.get()
		imgname = imgurl.split('/')[-1]
		imglocalpath = os.path.join(imgpath, imgname)
		img = requests.get(imgurl, headers)
		with open(imglocalpath, 'wb') as f:
			f.write(img.content)

class DouBanNovelRankParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.novels = []
		self._new_novel_img = False
		self._new_novel_info = False

	def handle_starttag(self, tag, attrs):

		def _getattr(attrname):
			for (k, v) in attrs:
				if attrname == k:
					return v
			return None

		if tag == 'li' and _getattr('class') == 'subject-item':
			self.novels.append(Novel())

		if self._new_novel_img == False and tag == 'div' and _getattr('class') == 'pic':
			self._new_novel_img = True

		if self._new_novel_img == True and tag == 'img':
			self.novels[-1].attrs.append(('novel_img_url', _getattr('src')))
			# print self.novels[-1].attrs
			global imgQueue
			imgQueue.put(_getattr('src'))

		if self._new_novel_info == False and tag == 'div' and _getattr('class') == 'info':
			self._new_novel_info = True

		if self._new_novel_info == True and tag == 'a':
			self.novels[-1].attrs.append(('novel_url', _getattr('href')))
			self.novels[-1].attrs.append(('novel_name', _getattr('title')))
			novel_name_tuple = self.novels[-1].attrs[-1]
			print novel_name_tuple[1]
			print self.novels[-1].attrs


	def handle_endtag(self, tag):
		if self._new_novel_img == True or self._new_novel_info == True:
			self._new_novel_img = False
			self._new_novel_info = False


if __name__ == '__main__':
	t1 = time.time()
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115'}
	x = requests.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', headers=headers)
	novelparser = DouBanNovelRankParser()
	novelparser.feed(x.content)
	parent_dir = os.path.dirname(os.path.abspath(__file__))
	imgpath = os.path.join(parent_dir, 'doubannovelimg')
	if not os.path.exists(imgpath):
		os.makedirs(imgpath)

	# for m in novelparser.novels:
	# 	m.downloadImg(imgpath, headers)

	threads = [Thread(target=imgDownLoader,args=[imgpath,headers]) for i in range(6)]
	for t in threads:
		t.start()
	for t in threads:
		t.join()

	print time.time()-t1
