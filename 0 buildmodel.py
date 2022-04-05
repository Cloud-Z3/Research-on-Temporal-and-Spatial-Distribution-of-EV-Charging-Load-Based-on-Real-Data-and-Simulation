import pandas as pd
import numpy as np
import os
import gc
import time
def start_end(df1):
    df2=np.zeros((df1.shape[0]),dtype=int) #创建数据行长度的0向量
    for i in range (df1.shape[0]):
        print('1:',i)
        if i==0:
            if df1[i][3]==1:
                df2[i]=1#1为订单起点，2为订单终点
        elif i==df1.shape[0]-1:
            if df1[i][3]==1:
                df2[i]=2
        else:
            if df1[i-1][3]==0 and df1[i][3]==1:
                df2[i]=1
            elif df1[i+1][3]==0 and df1[i][3]==1:
                df2[i]=2
            elif df1[i][0]!=df1[i-1][0] and df1[i][3]==1 and df1[i-1][3]==1:#司机数据结束与开始
                df2[i]=1
                df2[i-1]=2
            elif df1[i][0]!=df1[i+1][0] and df1[i][3]==1 and df1[i+1][3]==1:
                df2[i]=2
                df2[i+1]=1
    return df2#df2为一行向量，长度为数据集行数，确定订单起始np.zeros(dtype)

def screening(df1):
    m=1000000
    n=7
    df2=[[0 for j in range(n)] for i in range(m)]
    k=0
    flag=False
    print(df1.shape[1])
    for i in range(df1.shape[0]):
        print('2:',i)
        if df1[i][4]==1:
            df2[k][0]=df1[i][0]
            df2[k][1] = df1[i][1]
            df2[k][2] = df1[i][2]
            df2[k][3] = df1[i][3]
            flag=True
        if df1[i][4]==2 and flag and df2[k][0]==df1[i][0]:
            df2[k][4] = df1[i][1]
            df2[k][5] = df1[i][2]
            df2[k][6] = df1[i][3]
            k+=1
            flag=False
    #for i in df2:
        #print(i)
    return df2,k

path1='.\\0 raw_data'
path2='.\\1 trajectory'
dirs =os.listdir(path1)

t1=time.time()
for file in dirs:
    df=pd.read_csv(path1+'\\'+file,encoding='gbk')
    print(df)
    datetime=list(df['日期时间'])
    for i in df.index:
        datetime[i]=datetime[i].split(' ')[1].split(':')[0]
    df['日期时间']=datetime
    now=np.array(df)
    temp=start_end(now)

    df["起点终点"]=temp.tolist()#df1为起点终点列，作为新一行写入
    df=df[df['起点终点'].isin([1,2])]
    df=df[['司机编号','纬度','经度','日期时间','起点终点']]
    now=np.array(df)
    temp,num=screening(now)
    df=pd.DataFrame(data=temp[:num],columns=['司机编号','起点纬度','起点经度','起点时间','终点纬度','终点经度','终点时间'])
    df.to_csv(path2+'\\'+'dd_'+file,index=False,sep=',',encoding='utf_8_sig')
    del df
    gc.collect()
t2=time.time()
print(t2-t1)