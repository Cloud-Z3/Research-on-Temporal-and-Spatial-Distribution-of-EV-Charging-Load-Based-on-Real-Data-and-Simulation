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

dirs =os.listdir('.\\2 after_wash')
print(dirs)
start=[]
end=[]
for dir in dirs:
    df_dir=pd.read_csv('.\\2 after_wash\\'+dir)
    for i in df_dir.index:
        start.append([df_dir.iloc[i]['起点经度'],df_dir.iloc[i]['起点纬度']])
        end.append([df_dir.iloc[i]['终点经度'], df_dir.iloc[i]['终点纬度']])
plt.scatter([i[0] for i in start],[i[1] for i in start],s=4)
plt.savefig('.\\6 DataAna\\startPointShow.png')
plt.show()
plt.close()
plt.scatter([i[0] for i in end],[i[1] for i in end],s=0.1)
plt.savefig('.\\6 DataAna\\endPointShow.png')
plt.show()
plt.close()
