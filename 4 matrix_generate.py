import os
import pandas as pd
import time
import numpy as np
import scipy.io as io
import re

def solve1(a,x,now):  # a为最终需要的矩阵，x为订单起点数据集，y为订单终点数据集，now为当前矩阵层数
    for now_x in x.itertuples():#遍历dataframe
        a[now][int(now_x.起点归类)][int(now_x.终点归类)]+=1
    return a#转移矩阵

def solve2(a,x,now,tran):# a为最终需要的矩阵，x为订单起点数据集，y为订单终点数据集，now为当前矩阵层数
    for now_x in x.itertuples():
        a[now][int(now_x.起点归类)][int(now_x.终点归类)]+=now_x.时间/tran[now][int(now_x.起点归类)][int(now_x.终点归类)]
    return a#转移时间

def solve3(a,x,now,tran):# a为最终需要的矩阵，x为订单起点数据集，y为订单终点数据集，now为当前矩阵层数
    for now_x in x.itertuples():
        a[now][int(now_x.起点归类)][int(now_x.终点归类)] += now_x.距离/ tran[now][int(now_x.起点归类)][int(now_x.终点归类)]
    return a#转移距离

time_start = time.time()
mat_path1 = ".\\5 transfer_mat\\data.mat"#保存路径
path = ".\\4 after_clussify"  # 输入文件路径
dirs = os.listdir(path)
dirs.sort()

trans = np.zeros((63,300,300))
times = np.zeros((63,300,300))
distance = np.zeros((63,300,300))
time_num = ["06:00:00", "08:00:00", "10:00:00", "12:00:00", "14:00:00", "16:00:00", "18:00:00", "20:00:00", "22:00:00", "24:00:00"]

for i in range(len(dirs)):
    df=pd.read_csv(path+"\\"+dirs[i])
    time_data = df["起点时间"][0].split(" ")[0] # 提取日期
    for j in range(9):
        df_t = df[(df["起点时间"] >= time_data +time_num[j]) & (df["起点时间"] < time_data + time_num[j+1])]\
            .reset_index(drop=True)   # 提取对应时间段
        trans=solve1(trans,df_t,((int(re.split('[._]',dirs[i])[1])+3)%7)*9+j)#转移矩阵
        #最后的参数计算出当前数据为周几的哪个时间段，对应到矩阵的层数
        times=solve2(times,df_t,((int(re.split('[._]',dirs[i])[1])+3)%7)*9+j,trans)#时间矩阵
        distance = solve3(distance, df_t, ((int(re.split('[._]', dirs[i])[1]) + 3) % 7) * 9 + j, trans)  # 距离矩阵
    time_end = time.time()
    print(time_end - time_start)
trans=np.transpose(trans,(1,2,0))#将数组的axis重新进行排列,适用于matlab
times=np.transpose(times,(1,2,0))
distance=np.transpose(distance,(1,2,0))
io.savemat(mat_path1, {'trans': trans,"times":times,"distance":distance})#保存在一个mat类型文件中
