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

for i in range(1,5):
    #plt.subplot(2,2,i)
    #plt.plot([2,3],[3,4])
    ...
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
plt.show()
f(n)=f(n-1)+f(n-2)
f(n-1)=f(n-2)+f(n-3)
...
f(3)=f(2)+f(1)

f(n)=f(n-2)+f(n-3)+...+f(2)+f(1)+2
f1=1
f2=2
f3=3
f4=5
f5=8