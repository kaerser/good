#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/21 22:25
"""

def factorial(num):
	if num == 0:
		return 1
	if num >=1:
		return factorial(num-1)*num

if __name__ == "__main__":
	# 键盘输入需要计算的数值
	input_num = int(raw_input("请输入需要计算的数字： "))
	# 对输入的数值进行校对
	if input_num < 0:
		print "你所输入的值小于零，程序将退出！"
		quit()
	elif input_num > 10:
		print "你所输入的值过大，程序将退出！"
		quit()
	else:
		print "%d 的阶乘结果为： %d " % (input_num,factorial(input_num))