#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/18 16:13
"""
import csv,numpy
from datetime import datetime

if __name__ == '__main__':
	# with open('./ag0613.csv','rb') as csvfile:
	# 	read_data = csv.reader(csvfile)
	# 	for i in read_data:
	# 		print i
	# 	csvfile.close()

	start_time = datetime.now()
	csv_txt = numpy.loadtxt(open('ag0613.csv','rb'),skiprows=1)
	print '总共的数据量为：%d 条' % len(csv_txt)
	print '最大值为：%d ，最小值为：%d ，均值为：%d ，标准差为：%d ，中位数为：%d' % (csv_txt.max(),csv_txt.min(),csv_txt.mean(),csv_txt.std(),numpy.median(csv_txt))
	print '本次操作总计耗时：%d ms' % (datetime.now()-start_time).microseconds

