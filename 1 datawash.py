import os
import pandas as pd
from geographiclib.geodesic import Geodesic
import time
import numpy as np

def dd_time(df1):
    t=np.zeros((df1.shape[0],))
    for i in range(df1.shape[0]):
        start_time=df1[i][3]
        if (start_time.count(':') == 1):
            start_time += ':00'
        end_time = df1[i][6]
        if (end_time.count(':') == 1):
            end_time += ':00'

        t[i]=time.mktime(time.strptime(end_time,'%Y/%m/%d %H:%M:%S'))-time.mktime(time.strptime(start_time,'%Y/%m/%d %H:%M:%S'))
    return t

def dd_list(df1):
    x1 = df1[:,1].tolist()
    y1 = df1[:, 2].tolist()
    x2 = df1[:, 4].tolist()
    y2 = df1[:, 5].tolist()
    node=[]
    for i in range(len(x1)):
        dis=Geodesic.WGS84.Inverse(x1[i],y1[i],x2[i],y2[i])['s12']
        node.append(dis)
    return node

time_start = time.time()
path = ".\\1 trajectory"#输入文件路径
path2 = ".\\2 after_wash"#输入文件路径
dirs = os.listdir(path) #获取文件路径下的所有文件名

for file in dirs:
    df = pd.read_csv(path+"\\"+file) #完整的文件路径
    now=np.array(df)
    temp=dd_time(now)
    df['时间']=temp.tolist()
    now=np.array(df)
    temp=dd_list(now)
    df['距离']=temp
    df=df[(df['距离']>200)&(df['时间']>60)]
    ti=np.array(df['时间'])
    d=np.array((df['距离']))
    temp=d/ti
    df['速度']=temp
    df=df[(df['速度']>2)&(df['速度']<20)]
    df.to_csv(path2+'\\'+file,index=False,sep=',',encoding='utf_8_sig')
    time_end=time.time()
    print(time_end-time_start)
