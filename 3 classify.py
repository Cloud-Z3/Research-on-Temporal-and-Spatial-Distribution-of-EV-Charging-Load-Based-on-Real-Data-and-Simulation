import os
import pandas as pd
import time
import numpy as np

def dist(a,b,ax=1):
    return np.linalg.norm(a-b,axis=ax)#欧式距离

time_start=time.time()
path0='.\\2 after_wash'
path1=".\\3 cluster_result"#输入文件路径
path2=".\\4 after_clussify"#输出文件路径
dirs0=os.listdir(path0)#获取文件路径下的所有文件名
dirs1=os.listdir(path1)#获取文件路径下的所有文件名
for file in dirs0:
    dot=pd.read_csv(".\\3 cluster_result\\k_means_"+file)#输入聚类点信息
    print(dot)
    x_dot=dot["纬度"].tolist()#获取聚类点经纬度
    y_dot=dot["经度"].tolist()
    C=np.array(list(zip(x_dot,y_dot)))#聚类点中心

    df=pd.read_csv(path0+"\\"+file)#完整的文件路径
    x1=df["起点纬度"]#获取待分类点经纬度
    y1=df["起点经度"]
    x2=df["终点纬度"]#获取待分类点经纬度
    y2=df["终点经度"]
    X1=np.array(list(zip(x1,y1)))
    X2=np.array(list(zip(x2,y2)))
    node1=[]
    node2=[]
    for i in range(len(df)):
        distances = dist(X1[i], C, 1)
        now = np.argmin(distances)
        node1.append(dot['中心点编号'][now])
        distances = dist(X2[i], C, 1)
        now = np.argmin(distances)
        node2.append(dot['中心点编号'][now])
    df['起点归类'] = node1
    df['终点归类'] = node2
    df.to_csv(path2 + '\\' + file, index=False, sep=',', encoding='utf_8_sig')
    time_end = time.time()
    print(time_end - time_start)