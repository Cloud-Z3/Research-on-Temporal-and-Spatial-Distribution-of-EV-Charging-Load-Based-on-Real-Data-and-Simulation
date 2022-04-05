import pandas as pd
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
import time
import os
import math
import scipy.io as scio
import seaborn as sns
import matplotlib
#matplotlib.rcParams['font.sans-serif']=['Times New Roman'] #显示中文标签
matplotlib.rcParams['font.sans-serif']=['KaiTi'] #显示中文标签

df_km=pd.read_csv('.\\3 cluster_result\\k_means_merge(after POI).csv',encoding='gbk')#中心点
df_fri=pd.read_csv('.\\7 AnotherData\\Change\\data_fri1.csv',error_bad_lines=False)['fri']
df_sat=pd.read_csv('.\\7 AnotherData\\Change\\data_sat1.csv',error_bad_lines=False)['sat']

'''
df=pd.DataFrame({
    '工作日':df_fri['fri'],
    '周末':df_sat['sat']
})'''

matrix=[]
for i in range(1440):
    matrix.append([i / 60, df_fri[i]/10**6, '工作日'])
    matrix.append([i / 60, df_sat[i]/10**6, '周  末'])
df=pd.DataFrame(matrix,columns=['时间(h)','负荷(${×10^6kW}$)',''])

font={#'family':'serif',
     'style':'italic',
    'weight':'normal',
      'color':'black',
      'size':16
}

sns.lineplot(data=df,x='时间(h)',y='负荷(${×10^6kW}$)',hue='')
#fig,ax=plt.subplots(111)
plt.plot([6,6],[0,max(max(df_fri),max(df_sat))/10**6],'g--')
#plt.legend(labels=["工作日","周末"])
plt.axis([0,24,0,max(max(df_fri),max(df_sat))/10**6])
plt.xticks([0,4,6,8,12,16,20,24],font={'family':'Times New Roman'})
plt.yticks([0,0.5,1,1.5,2,2.5],font={'family':'Times New Roman'})
plt.xlabel('时间(h)',fontdict={'size':13})
plt.ylabel('负荷(${×10^6kW}$)',fontdict={'size':13})
#plt.xticks(fontsize=10)
plt.text(3, 1.5, s="慢\n充\n模\n式",fontdict=font)
plt.text(15, 1.5, s="快\n充\n模\n式",fontdict=font)
#ax.ticklabel_format(useOffset=False)
plt.savefig('.\\6 DataAna\\LoadWithTime7.png',dpi=4500)
#plt.show()
#print(changelow)
'''
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
'''
#plt.savefig(".\\3 cluster_result\\k_means_merge_new"+".png")
#plt.show()
'''
time_end=time.time()

print('程序运行时间为', time_end - time_start)'''