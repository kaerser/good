#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author = 'Administrator'
@time: 17/01/08 下午 03:48
"""

from __future__ import division
from numpy.random import randn
import numpy as np
import os
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
	df = DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
	df.plot(kind='bar')
	plt.show()


