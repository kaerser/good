#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 04:42
"""

# 对macrodata.csv数据集，画出realgdp列的直方图， 画出realgdp列与realcons列的散点图，初步判断两个变量之间的关系

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
	plt.figure()
	macro_file = './data/macrodata.csv'
	macro_data = pd.read_csv(macro_file)
	print macro_data[['realgdp','realcons']]
	macro_data['realgdp'].hist(bins=len(macro_data),color='g')
	plt.scatter(macro_data['realgdp'],macro_data['realcons'])
	plt.show()
