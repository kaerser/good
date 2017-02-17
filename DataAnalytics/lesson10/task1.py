#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/02/10 下午 04:17
"""

from numpy import *
import pandas as pd
import seaborn as sns
import matplotlib
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
	data = {
		'snow': [5.1, 3.5, 7.1, 6.2, 8.8, 7.8, 4.5, 5.6, 8.0, 6.4],
		'irrigation': [1907, 1287, 2700, 2373, 3260, 3000, 1947, 2273, 3113,2493]
	}
	snow_irrigation = DataFrame(data)
	# sns.jointplot(x='snow',y='irrigation',data=snow_irrigation)
	sns.pairplot(snow_irrigation, x_vars='snow', y_vars='irrigation', size=7, aspect=0.8,kind='reg')
	print snow_irrigation.corr()
	sns.plt.show()

	x = snow_irrigation['snow']
	y = snow_irrigation['irrigation']
	linreg = LinearRegression()
	linreg.fit(x.values.reshape(len(x), 1), y)
	print '截距为：',linreg.intercept_
	print '回归系数为：',linreg.coef_
