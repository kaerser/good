#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/02/17 下午 02:39
"""

from numpy import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame
from sklearn.linear_model import LinearRegression
from sklearn import metrics

if __name__ == "__main__":
	data2 = pd.read_table('./data/data2.txt',sep='\t')
	x = data2['X']
	y = data2['Y']
	linreg = LinearRegression()
	linreg.fit(x,y)
	print('Coefficients: \n', linreg.coef_)
	y_pred = linreg.predict(x)
	print "MSE:",metrics.mean_squared_error(y,y_pred)



