#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/3/19 10:29
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_table('./data/ex15.txt',index_col =0,header = 0,sep='\s')
print df

X=df.iloc[:,0:3]
y=df['"y"']

# 使用原数据 3 个自变量线性回归
linreg = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=1)
linreg.fit(X_train, y_train)
print linreg.intercept_
print linreg.coef_
print zip(['x1','x2','x3'], linreg.coef_)
y_pred = linreg.predict(X_test)
print "MAE:",metrics.mean_absolute_error(y_test,y_pred)
print "MSE:",metrics.mean_squared_error(y_test,y_pred)
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))

# 使用主成分分析结果，一个主变量回归分析
pca = PCA(n_components=1)
reduced_X = pca.fit_transform(X)
X_train, X_test, y_train, y_test =train_test_split(reduced_X, y, random_state=1)
linreg.fit(X_train, y_train)
print linreg.intercept_
print linreg.coef_
print zip(['reduced_X'], linreg.coef_)
y_pred = linreg.predict(X_test)
print "MAE:",metrics.mean_absolute_error(y_test,y_pred)
print "MSE:",metrics.mean_squared_error(y_test,y_pred)
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred))