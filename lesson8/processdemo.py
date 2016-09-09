#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:9/8/2016 03:20 PM
"""
from multiprocessing import Process,current_process
import time

def work():
	while True:
		print 'In worker %s' % current_process()
		time.sleep(1)

if __name__ == '__main__':
	ps = [Process(target=work) for i in range(3)]
	for p in ps:
		p.start()
	for p in ps:
		p.join()