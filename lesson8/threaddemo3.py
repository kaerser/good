#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:9/8/2016 02:59 PM
"""
from threading import Thread,current_thread,Condition
import time

class Producer(Thread):
	def __init__(self,datacache,lock):
		Thread.__init__(self)
		self._dc = datacache
		self._l = lock

	def run(self):
		i = 0
		while True:
			msg = 'From Producer Msg is : %d' % i
			self._l.acquire()
			self._dc.append(msg)
			self._l.notify_all()
			self._l.release()
			time.sleep(0.2)
			i += 1

class Consumer(Thread):
	def __init__(self,datacache,lock):
		Thread.__init__(self)
		self._dc = datacache
		self._l = lock

	def run(self):
		while True:
			self._l.acquire()
			while len(self._dc) == 0:
				self._l.wait()
			msg = self._dc.pop()
			self._l.release()
			print 'Consumer %s Receive : %s' % (current_thread(),msg)
			time.sleep(1)

if __name__ == '__main__':
	datacache = []
	lock = Condition()

	producer1 = Producer(datacache,lock)
	producer1.start()

	consumers = [Consumer(datacache,lock) for i in range(4)]
	for c in consumers:
		c.start()

	producer1.join()
	for c in consumers:
		c.join()