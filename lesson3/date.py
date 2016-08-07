#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/8/7 21:09
"""


def check_date(year, month, kwargs):
	# 日期初始值
	init_date = {'year': 1990, 'month': 1, 'day': 1}

	# 年份差额
	x = int(year) - init_date['year']
	if x <= 2:
		l = 365 * x
	else:
		l = 365 * 2 + 366 + ((x - 2) % 4 - 1) * 365 + (x / 4) * (366 + 365 * 3)

	y = 0
	for k, v in kwargs.items():
		if int(month) >= k:
			y = y + v

	sum = l + y
	return sum % 7


def add(kwargs):
	# return sum(kwargs.values())
	print kwargs

if __name__ == "__main__":
	# 定义日历字典
	leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 30}
	not_leap_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 30}

	# 输入需要查询的日历信息
	input_year = raw_input("请输入你想查询的年份(1990年以后)：")
	input_month = raw_input("请输入你想查询的月份(1-12)：")

	if int(input_month) > 0 and int(input_month) < 13:
		pass
	else:
		print "请输入正确的月份数字！！"
		exit()

	# 判断输入的年份是否为闰年
	if (int(input_year) % 4 == 0 and int(input_year) % 100 != 0) or (int(input_year) % 400 == 0):
		print "你所输入的年份为闰年"
		# add(leap_year)
		n = check_date(input_year,input_month,leap_year)
		print "你输入的日期%s年%s月%d日是星期%s" % (input_year,input_month,leap_year[int(input_month)],n+1)
	else:
		print "你所输入的年份不是闰年"
		# add(**not_leap_year)
		n = check_date(input_year, input_month, not_leap_year)
		print "你输入的日期%s年%s月%d日是星期%s" % (input_year,input_month,not_leap_year[int(input_month)],n+1)
