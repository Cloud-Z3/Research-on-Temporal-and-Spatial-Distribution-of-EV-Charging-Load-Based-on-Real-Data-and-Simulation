import pandas as pd
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
import time
import os


def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)  # 计算欧氏距离


def k_means(X, k ):
    # 随机获得中心点的X轴坐标
    C_x = np.random.uniform(103.8, 104.2, size=k)  # 功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high. size: 输出样本数目
    # C_x = np.random.uniform(np.min(X,axis=0)[0],np.max(X,axis=0)[0],size=k)
    # 随机获得中心点的Y轴坐标
    C_y = np.random.uniform(30.5, 30.8, size=k)  # k个中心点
    # C_y = np.random.uniform(np.min(X,axis=0)[1],np.max(X,axis=0)[1],size=k)
    C = np.array(list(zip(C_x, C_y)))  # 成矩阵，中心点矩阵，列x，列y

    # 用于保存中心点更新前的坐标
    C_old = np.zeros(C.shape)  # 相同行列数的零矩阵，用于保存中心点更新前的坐标
    # 用于保存数据所属中心点
    clusters = np.zeros(len(X))
    # 迭代标识位，通过计算新旧中心点的距离
    iteration_flag = dist(C, C_old, 1)
    tmp = 1
    while (iteration_flag > 1e-2).any():  # 任意一个元素为True
        # 循环计算出每个点对应的最近中心点
        for i in range(len(X)):
            # 计算出每个点与中心点的距离
            distances = dist(X[i], C, 1)
            # 记录0 - k-1个点中距离近的点
            cluster = np.argmin(distances)
            # 记录每个样例点与哪个中心点距离最近
            clusters[i] = cluster

        # 采用深拷贝将当前的中心点保存下来
        C_old = deepcopy(C)
        # 从属于中心点放到一个数组中，然后按照列的方向取平均值
        for i in range(k):
            points = [X[j] for j in range(len(X)) if clusters[j] == i]
            if len(points) != 0:
                C[i] = np.mean(points, axis=0)

        # 计算新旧节点的距离
        print("循环第%d次" % tmp)
        tmp = tmp + 1
        iteration_flag = dist(C, C_old, 1)
    colormap=plt.cm.gist_ncar
    colorst = [colormap(i) for i in np.linspace(0, 0.9, k)]
    index = 0
    C_del = []
    C_index = np.arange(k)
    C = np.insert(C, 2, C_index, axis=1)
    for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        if len(points) != 0:
            index += 1
            plt.scatter(points[:, 0], points[:, 1], s=6, color=colorst[i])
        else:
            C_del.append(i)
    C = np.delete(C, C_del, axis=0)
    plt.scatter(C[:, 0], C[:, 1], marker='*', s=20, color='black')
    #plt.savefig(".\\3 cluster_result\\k_means_"+file[:-4]+".png")
    #plt.show()
    print('有效中心点数为', index)
    return C


time_start = time.time()
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
path=".\\2 after_wash"#输入文件路径
path2=".\\3 cluster_result"#输出文件路径
dirs=os.listdir(path)#获取文件路径下的所有文件名
df=pd.read_csv('.\\2 after_wash\\'+dirs[0])
for i in range(1,len(dirs)):
    print(dirs[i])
    data = pd.read_csv(path+'\\'+dirs[i])
    df=pd.concat([df,data])
f1 = df['起点经度'].values
f2 = df['终点纬度'].values
X1 = np.array(list(zip(f1, f2)))
f1=df['终点经度'].values
f2=df['终点纬度'].values
X1=np.append(X1,np.array(list(zip(f1,f2))),axis=0)
dots=k_means(X1,300)

# 保存数据
df = pd.DataFrame(dots)
df.columns = ["经度", "纬度", "中心点编号"]
df.to_csv(".\\3 cluster_result\\k_means_merge.csv", index=False, sep=",", encoding='utf_8_sig')
time_end = time.time()
print('程序运行时间为', time_end - time_start)