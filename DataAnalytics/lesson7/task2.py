#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 05:08
"""

# 对tips数据集，画出size的饼图

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd

if __name__ == "__main__":
	tips_file = './data/tips.csv'
	tips_data = pd.read_csv(tips_file)
	lab = tips_data['size'].unique()
	size_data = pd.cut(tips_data['size'],6,labels=lab)
	print size_data.value_counts()
	plt.pie(size_data.value_counts(), labels=lab,autopct='%1.1f%%', startangle=67)
	plt.title('tips for size')
	plt.show()
