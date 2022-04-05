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
sns.set(style='ticks')
matplotlib.rcParams['font.sans-serif']=['KaiTi'] #显示中文标签

filename_workday='dd_18.csv'
filename_weekend='dd_23.csv'
kmeansfile_workday='k_means_dd_18.csv'
kmeansfile_weekend='k_means_dd_23.csv'
df_data1=pd.read_csv('.\\4 after_clussify\\'+filename_workday)
df_data2=pd.read_csv('.\\4 after_clussify\\'+filename_weekend)
df_kind1=pd.read_csv('.\\7 AnotherData\\kmeansKind\\'+kmeansfile_workday,encoding='gbk')
df_kind2=pd.read_csv('.\\7 AnotherData\\kmeansKind\\'+kmeansfile_weekend)


id_kind1=dict() #聚类中心点与分区的对应关系
id_kind2=dict()

for i in df_kind1.index:
    id_kind1[df_kind1['中心点编号'][i]]=df_kind1['分区'][i]
print(id_kind1)

for i in df_kind2.index:
    id_kind2[df_kind2['中心点编号'][i]]=df_kind2['分区'][i]
print(id_kind2)
#工作日与周末各时段平均出行量分布对比
#根据POI分类
kind=[]
for i in df_kind1.index:
    if df_kind1['分区'][i] not in kind:
        kind.append(df_kind1['分区'][i])
print(kind)

def lineplot():
    index=1
    for k in kind:
        time_order1 = dict()
        for i in df_data1.index:
            if id_kind1[int(df_data1['起点归类'][i])]==k:
                time=df_data1['起点时间'][i].split(' ')[1].split(':')[0]
                if int(time) not in time_order1:
                    time_order1[int(time)] = 1
                else:
                    time_order1[int(time)] += 1
        for i in range(24):
            if i not in time_order1:
                time_order1[i]=0
        order1=[time_order1[i] for i in range(24)]#工作日起点

        time_order2=dict()
        for i in df_data2.index:
            if id_kind2[int(df_data2['起点归类'][i])] == k:
                time=df_data2['起点时间'][i].split(' ')[1].split(':')[0]
                if int(time) not in time_order2:
                    time_order2[int(time)] = 1
                else:
                    time_order2[int(time)] += 1
        for i in range(24):
            if i not in time_order2:
                time_order2[i]=0
        order2=[time_order2[i] for i in range(24)]#周末起点

        time_order3 = dict()
        for i in df_data1.index:
            if id_kind1[int(df_data1['终点归类'][i])] == k:
                time = df_data1['终点时间'][i].split(' ')[1].split(':')[0]
                if int(time) not in time_order3:
                    time_order3[int(time)] = 1
                else:
                    time_order3[int(time)] += 1
        for i in range(24):
            if i not in time_order3:
                time_order3[i] = 0
        order3 = [time_order3[i] for i in range(24)]  # 工作日终点

        time_order4 = dict()
        for i in df_data2.index:
            if id_kind2[int(df_data2['终点归类'][i])] == k:
                time = df_data2['终点时间'][i].split(' ')[1].split(':')[0]
                if int(time) not in time_order4:
                    time_order4[int(time)] = 1
                else:
                    time_order4[int(time)] += 1
        for i in range(24):
            if i not in time_order4:
                time_order4[i] = 0
        order4 = [time_order4[i] for i in range(24)]  # 周末终点
        plt.subplot(2,2,index)
        index+=1
        df_time_order=pd.DataFrame([[i+1,order1[i],order3[i],order2[i],order4[i]] for i in range(24)],index=range(24),columns=['时间（时）','工作日（订单起点）','工作日（订单终点）','周 末（订单起点）','周 末（订单终点）'])
        sns.lineplot(data=df_time_order,x='时间（时）',y=['工作日（订单起点）','工作日（订单终点）','周 末（订单起点）','周 末（订单终点）'])
        plt.xticks([i for i in range(1,25,6)])
        plt.xlabel('时间(时)')
        plt.ylabel('订单次数(次)')


        plt.savefig('.\\6 DataAna\\order_time_workday&weekend_start&end2'+k+'.jpg')
        plt.show()
        plt.close()

lineplot()
