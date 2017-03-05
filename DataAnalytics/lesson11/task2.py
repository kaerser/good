#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/2/19 20:35
"""
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
	data_file = './data/data2.txt'
	data_all = pd.read_table(data_file)
	data2 = data_all[['X','Y']]
	x = data2['X']
	y = data2['Y']

	# 线性回归模型
	x = np.array(x).reshape(len(x),1)
	linreg = LinearRegression()
	linreg.fit(x,y)
	print '线性回归 Coefficients: ', linreg.coef_
	y_pred = linreg.predict(x)
	print "线性回归 MSE:",metrics.mean_squared_error(y,y_pred)
	print('线性回归 Variance score: %.2f' % linreg.score(x, y))

	# 多项式模型
	x1=x
	x2=x**2
	x1['x2']=x2
	linreg = LinearRegression()
	linreg.fit(x1,y)
	print('多项式模型 Coefficients: ', linreg.coef_)
	y_pred = linreg.predict(x)
	print "多项式模型 MSE:",metrics.mean_squared_error(y,y_pred)

	# 对数模型
	x2=pd.DataFrame(np.log(x[0]))
	linreg = LinearRegression()
	linreg.fit(x2,y)
	print('对数模型 Coefficients: \n', linreg.coef_)
	y_pred = linreg.predict(x2)
	print "对数模型 MSE:",metrics.mean_squared_error(y,y_pred)

	# 指数模型
	y2=pd.DataFrame(np.log(y))
	linreg = LinearRegression()
	linreg.fit(pd.DataFrame(x[0]),y2)
	print('指数模型 Coefficients: \n', linreg.coef_)
	y_pred = linreg.predict(pd.DataFrame(x[0]))
	print "指数模型 MSE:",metrics.mean_squared_error(y2,y_pred)

	# 幂函数模型
	linreg = LinearRegression()
	linreg.fit(x2,y2)
	print('幂函数模型 Coefficients: \n', linreg.coef_)
	y_pred = linreg.predict(x2)
	print "幂函数模型 MSE:",metrics.mean_squared_error(y2,y_pred)






