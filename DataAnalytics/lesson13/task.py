#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/3/5 16:39
"""

import numpy as np
from pandas import DataFrame
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
	my_data=[
		['slashdot','USA','yes',18,'None'],
		['google','France','yes',23,'Premium'],
		['digg','USA','yes',24,'Basic'],
		['kiwitobes','France','yes',23,'Basic'],
		['google','UK','no',21,'Premium'],
		['(direct)','New Zealand','no',12,'None'],
		['(direct)','UK','no',21,'Basic'],
		['google','USA','no',24,'Premium'],
		['slashdot','France','yes',19,'None'],
		['digg','USA','no',18,'None'],
		['google','UK','no',18,'None'],
		['kiwitobes','UK','no',19,'None'],
		['digg','New Zealand','yes',12,'Basic'],
		['slashdot','UK','no',21,'None'],
		['google','UK','yes',18,'Basic'],
		['kiwitobes','France','yes',19,'Basic']
	]

	# 数据整理
	col=['source','country','readOrNot','pageviews','target']
	data=DataFrame(my_data,columns=col)
	data['source']=pd.Categorical(data['source']).codes
	data['country']=pd.Categorical(data['country']).codes
	data['readOrNot']=pd.Categorical(data['readOrNot']).codes
	data['pageviews']=pd.Categorical(data['pageviews']).codes
	data['target']=pd.Categorical(data['target']).codes
	data=DataFrame(data,dtype=np.int64)
	x=data.iloc[:,:4].as_matrix()
	y=data.iloc[:,4].as_matrix()

	# 划分训练集和测试集
	x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

	# KNN
	clf = KNeighborsClassifier(algorithm='kd_tree')
	clf.fit(x_train, y_train)
	answer = clf.predict(x_test)
	print 'KNN-Precision:%s' % (np.mean( answer == y_test))

	# 贝叶斯分类器
	clf = BernoulliNB()
	clf.fit(x_train,y_train)
	answer = clf.predict(x_test)
	print 'Bayes-Precision:%s' % (np.mean( answer == y_test))

	# 决策树模型
	from sklearn.tree import DecisionTreeClassifier as DTC
	# 建立决策树模型，基于信息熵
	dtc = DTC(criterion='entropy')
	# 训练模型
	dtc.fit(x_train, y_train)
	# 导入相关函数，可视化决策树。
	# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
	from sklearn.tree import export_graphviz
	from sklearn.externals.six import StringIO
	with open("tree.dot", 'w') as f:
  		f = export_graphviz(dtc, out_file = f)
	answer = dtc.predict(x_test)
	print 'DecisionTree-Precision:%s' %(np.mean( answer == y_test))

	# SVM模型
	from sklearn.svm import SVC
	clf =SVC()
	clf.fit(x_train, y_train)
	answer = clf.predict(x_test)
	print 'SVM-Precision:',(np.mean( answer == y_test))