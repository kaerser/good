#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 05:28
"""

# 对tips数据集，画出不同sex与day的交叉表的柱形图

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
	crosstab_sex_day = pd.crosstab(tips_data['sex'],tips_data['day'])
	print crosstab_sex_day
	crosstab_sex_day.plot(kind='bar')
	plt.show()
