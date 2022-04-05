#本文件用于订单时长、平均速度、订单距离等分布的统计

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
filename='dd_03.csv'
df_data=pd.read_csv('.\\2 after_wash\\'+filename)
print(df_data['距离'])

for i in df_data.index:
    df_data['距离'][i] = df_data['距离'][i] / 1000
    if df_data['距离'][i]>22:
        del df_data['距离'][i]
    df_data['时间'][i] = df_data['时间'][i] / 60
    if df_data['时间'][i]>100:
        df_data['时间'][i]

#订单时长的分布
sns.histplot(df_data,x='时间',kde=True)
plt.xlabel('订单时长(min)')
plt.ylabel('频数')
#plt.show()
plt.savefig(".\\6 DataAna\\time_distribution1.png")
plt.close()

#订单平均速度的分布
sns.histplot(df_data,x='速度',kde=True)
plt.xlabel('平均速度(km/s)')
plt.ylabel('频数')
#plt.show()
plt.savefig(".\\6 DataAna\\speed_distribution1.png")
plt.close()

#订单距离的分布
sns.histplot(df_data,x='距离',kde=True)
plt.xlabel('订单距离(km)')
plt.ylabel('频数')
#plt.show()
plt.savefig(".\\6 DataAna\\distance_distribution1.png")
plt.close()

