#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/20 上午 09:20
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from scipy import stats as ss

if __name__ == "__main__":
	df=DataFrame({'data':[3.2,3.3,3.0,3.7,3.5,4.0,3.2,4.1,2.9,3.3]})
	print ss.ttest_1samp(a = df, popmean = 10)

	data_file = './data/Amtrak.xls'
	data1 = pd.read_excel(data_file)
	print data1.describe()
	print data1.skew()
	print data1.kurt()
