#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'kaerser'
@time:8/23/2016 05:28 PM
"""

# 转换IP为长整型数字
def ip2long(ip):
	list1 = ip.split('.')
	str = ''
	for i in list1:
		i = '0'*(3-len(i))+i
		str += i
	return int(str)

if __name__ == '__main__':
	IP1 = raw_input('请输入你需要转换的IP：')
	print ip2long(IP1)

