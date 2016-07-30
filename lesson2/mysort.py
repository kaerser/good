#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/7/30 23:09
"""

# 使用冒泡排序方法
def mysort(alist):
	list_len = len(alist)
	# print list_len
	if list_len < 2:
		return alist
	for i in range(list_len):
		for j in range(list_len-i-1):
			if alist[j] > alist[j+1]:
				alist[j],alist[j+1] = alist[j+1],alist[j]
	return alist

if __name__ == "__main__":
	list1 = [10,20,32,14,9,35,18,20]
	print mysort(list1)
