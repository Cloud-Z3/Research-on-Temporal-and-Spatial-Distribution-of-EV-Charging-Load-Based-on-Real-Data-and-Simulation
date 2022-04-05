import pandas as pd
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
import time
import os
import math

def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)  # 计算欧氏距离

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

time_start=time.time()
k=300
colormap=plt.cm.gist_ncar
colorst = [colormap(i) for i in np.linspace(0, 0.9, k)]
index = 0

df_km=pd.read_csv('.\\3 cluster_result\\k_means_merge(after POI).csv',encoding='gbk')#中心点
df_points=pd.read_csv('.\\2 after_wash\\dd_03.csv')#所有点
center=[]
print(df_km)
print(df_points)
for i in df_km.index:
    center.append([df_km.iloc[i]['经度'],df_km.iloc[i]['纬度']])
print(center)
for i in df_points.index:
    mindist=100
    index=0
    point=[df_points.iloc[i]['起点经度'],df_points.iloc[i]['起点纬度']]
    for j in range(k):
        if dist(center[j],point)<mindist:
            mindist=dist(center[j],point)
            index=j
    plt.scatter(point[0],point[1], s=6, color=colorst[index])

for i in range(k):
    plt.scatter(center[i][0],center[i][1], marker='*', s=20, color='black')

plt.savefig(".\\3 cluster_result\\k_means_merge_new"+".png")
plt.show()

time_end=time.time()

print('程序运行时间为', time_end - time_start)