#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author__ = 'kaerser'
@time:2017/3/12 13:11
"""

import os
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from __future__ import division

ex14 = pd.read_csv('./data/ex14.csv',header = 0,index_col = 0,parse_dates = True,encoding='gb18030')
ex14.head()
ex14.index
# 查看图形
fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(ex14['DXBZ'],ex14['CZBZ'],ex14['WMBZ'],marker='o')
ax3D.set_xlabel('DXBZ')
ax3D.set_ylabel('CZBZ')
ax3D.set_zlabel('WMBZ')
plt.show()

# cluster
for linkage in ('ward', 'average', 'complete'):
    clustering = AgglomerativeClustering(linkage=linkage, n_clusters=3)
    clustering.fit(ex14)
    cluster_pred = clustering.fit_predict(ex14)
    print 'clusters :',cluster_pred
    ex14[u'类型']=cluster_pred
    print ex14
    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    ax3D.scatter(ex14['DXBZ'],ex14['CZBZ'],ex14['WMBZ'],c=cluster_pred,marker='o')
    ax3D.set_xlabel('DXBZ')
    ax3D.set_ylabel('CZBZ')
    ax3D.set_zlabel('WMBZ')
    plt.show()

# kmeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(ex14)
kmeans_pred = kmeans.fit_predict(ex14)
print 'kmeans cluster:',kmeans_pred
ex14[u'类型']=kmeans_pred
print ex14
fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(ex14['DXBZ'],ex14['CZBZ'],ex14['WMBZ'],c=kmeans_pred,marker='o')
ax3D.set_xlabel('DXBZ')
ax3D.set_ylabel('CZBZ')
ax3D.set_zlabel('WMBZ')
plt.show()