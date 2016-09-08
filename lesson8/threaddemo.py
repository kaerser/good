#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:9/8/2016 01:10 PM
"""

from threading import Thread,current_thread,Lock
import time,sys

def worker():
	while True:
		# l.acquire()
		# print 'In worker %s' % current_thread()
		sys.stdout.write('In worker %s\n' % current_thread())
		# l.release()
		time.sleep(0.2)

if __name__ == '__main__':
	# 多线程同步锁
	# l = Lock()
	print 'In Main %s' % current_thread()
	threads = [Thread(target=worker) for i in range(10)]
	for t in threads:
		t.start()

	for t in threads:
		t.join()
