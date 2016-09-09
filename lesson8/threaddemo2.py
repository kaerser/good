#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:9/8/2016 01:24 PM
"""
from threading import Thread,current_thread,Lock
import time

class MyThread(Thread):
	def __init__(self,l):
		Thread.__init__(self)
		self._l = l

	def run(self):
		while True:
			self._l.acquire()
			print 'In Worker %s' % current_thread()
			self._l.release()
			time.sleep(0.5)

if __name__ == '__main__':
	l = Lock()
	print 'In main %s' % current_thread()
	threads = [MyThread(l) for i in range(5)]
	for t in threads:
		t.start()

	for t in threads:
		t.join()