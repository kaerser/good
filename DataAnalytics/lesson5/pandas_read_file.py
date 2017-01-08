#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2016/12/25 19:16
"""

import pandas,xlrd,xlwt
import numpy
from pandas import DataFrame
import requests,json

if __name__ == '__main__':
	# 读取csv文件数据
	df1 = pandas.read_csv('./data/Dress Sales.csv')
	print df1
	# 读取txt文件
	df2 = list(open('./data/creditcard-dataset.txt'))
	print len(df2)
	df2 = pandas.read_table('./data/creditcard-dataset.txt', sep=',', header=None)
	print df2
	# 读取xls文件
	wb = xlrd.open_workbook('./data/ApplianceShipments.xls')
	# print wb.sheet_names()
	sheet1 = wb.sheet_by_index(0)
	print sheet1.name,sheet1.ncols,sheet1.nrows
	xls_file = pandas.ExcelFile('./data/ApplianceShipments.xls')
	df3 = xls_file.parse(sheetname=sheet1.name,header=None)
	print df3
	#使用HTML和Web API
	url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
	resp = requests.get(url)
	print resp
	data_json = json.loads(resp.text)
	issue_lables = DataFrame(data_json)
	print issue_lables


