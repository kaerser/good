#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/02/12 下午 09:39
"""

import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
import matplotlib
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

if __name__ == "__main__":
	data = {
		'x1': [0.4, 0.4, 3.1, 0.6, 4.7, 1.7, 9.4, 10.1, 11.6, 12.6, 10.9, 23.1, 23.1, 21.6, 23.1, 1.9, 26.8, 29.9],
		'x2': [53, 23, 19, 34, 24, 65, 44, 31, 29, 58, 37, 46, 50, 44, 56, 36, 28, 51],
		'x3': [158, 163, 37, 157, 59, 123, 46, 117, 173, 112, 111, 114, 134, 73, 168, 143, 202, 124],
		'y': [64, 60, 71, 61, 54, 77, 81, 93, 93, 51, 76, 96, 77, 93, 95, 54, 168, 99]
	}
	data2 = DataFrame(data)
	linreg = LinearRegression()

	# 全变量
	x = data2[['x1', 'x2', 'x3']]
	y = data2['y']
	X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=1)
	linreg.fit(X_train, y_train)
	y_pred = linreg.predict(X_test)
	print "全变量MAE:", metrics.mean_absolute_error(y_test, y_pred)
	print "全变量MSE:", metrics.mean_squared_error(y_test, y_pred)
	print "全变量RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred))

	# 删除变量X1
	x_re_x1 = data2[['x2','x3']]
	X_re_x1_train, X_re_x1_test, y_re_x1_train, y_re_x1_test = train_test_split(x_re_x1, y, random_state=1)
	linreg.fit(X_re_x1_train, y_re_x1_train)
	y_re_x1_pred = linreg.predict(X_re_x1_test)
	print "删除变量X1 MAE:", metrics.mean_absolute_error(y_re_x1_test, y_re_x1_pred)
	print "删除变量X1 MSE:", metrics.mean_squared_error(y_re_x1_test, y_re_x1_pred)
	print "删除变量X1 RMSE:", np.sqrt(metrics.mean_squared_error(y_re_x1_test, y_re_x1_pred))

	# 删除变量X2
	x_re_x2 = data2[['x1','x3']]
	X_re_x2_train, X_re_x2_test, y_re_x2_train, y_re_x2_test = train_test_split(x_re_x2, y, random_state=1)
	linreg.fit(X_re_x2_train, y_re_x2_train)
	y_re_x2_pred = linreg.predict(X_re_x2_test)
	print "删除变量x2 MAE:", metrics.mean_absolute_error(y_re_x2_test, y_re_x2_pred)
	print "删除变量x2 MSE:", metrics.mean_squared_error(y_re_x2_test, y_re_x2_pred)
	print "删除变量x2 RMSE:", np.sqrt(metrics.mean_squared_error(y_re_x2_test, y_re_x2_pred))

	# 删除变量X3
	x_re_x3 = data2[['x1','x2']]
	X_re_x3_train, X_re_x3_test, y_re_x3_train, y_re_x3_test = train_test_split(x_re_x3, y, random_state=1)
	linreg.fit(X_re_x3_train, y_re_x3_train)
	y_re_x3_pred = linreg.predict(X_re_x3_test)
	print "删除变量x3 MAE:", metrics.mean_absolute_error(y_re_x3_test, y_re_x3_pred)
	print "删除变量x3 MSE:", metrics.mean_squared_error(y_re_x3_test, y_re_x3_pred)
	print "删除变量x3 RMSE:", np.sqrt(metrics.mean_squared_error(y_re_x3_test, y_re_x3_pred))
