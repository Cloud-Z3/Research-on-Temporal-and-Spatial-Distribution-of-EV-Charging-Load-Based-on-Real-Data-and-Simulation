#本文件用于各种指标的对比与图形绘制

import os
import pandas as pd
import time
import numpy as np
import scipy.io as io
import re
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
matplotlib.rcParams['font.sans-serif']=['KaiTi'] #显示中文标签

filename_workday='dd_03.csv'
filename_weekend='dd_04.csv'
kmeansfile_workday='k_means_dd_03.csv'
kmeansfile_weekend='k_means_dd_04.csv'
df_data1=pd.read_csv('.\\4 after_clussify\\'+filename_workday)
df_data2=pd.read_csv('.\\4 after_clussify\\'+filename_weekend)
#df_kind=pd.read_csv('.\\7 AnotherData\\kmeansKind\\'+kmeansfile_workday)
#工作日与周末各时段平均出行量分布对比
def lineplot(sORe):
    time_order1=dict()
    for i in df_data1.index:
        time=df_data1[sORe][i].split(' ')[1].split(':')[0]
        if int(time) not in time_order1:
            time_order1[int(time)] = 1
        else:
            time_order1[int(time)] += 1
    for i in range(24):
        if i not in time_order1:
            time_order1[i]=0
    order1=[time_order1[i] for i in range(24)]
    time_order2=dict()
    for i in df_data2.index:
        time=df_data2[sORe][i].split(' ')[1].split(':')[0]
        if int(time) not in time_order2:
            time_order2[int(time)] = 1
        else:
            time_order2[int(time)] += 1
    for i in range(24):
        if i not in time_order2:
            time_order2[i]=0
    order2=[time_order2[i] for i in range(24)]
    df_time_order=pd.DataFrame([[order1[i],order2[i]] for i in range(24)],index=range(24),columns=['工作日','周  末'])
    sns.lineplot(data=df_time_order)
    plt.xlabel('时间(时)')
    plt.ylabel('订单次数(次)')
    print(sORe)
    if sORe=='起点时间':
        print(1)
        plt.savefig('.\\6 DataAna\\order_time_workday&weekend(start)')
    if sORe=='终点时间':
        print(2)
        plt.savefig('.\\6 DataAna\\order_time_workday&weekend(end)')
    plt.show()

lineplot('起点时间')
lineplot('终点时间')