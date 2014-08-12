##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 得到每列的基本统计信息，均值，方差，标准方差等

import numpy as np
from StringIO import StringIO
''' 修改 numpy 打印设置 '''
np.set_printoptions(precision=3, ## 小数点后精度
                    linewidth = 120) ## 每行最大字符长度

''' 从txt文件中读取数据 '''
with open('copd_1100_train.txt', 'rb') as text:
    data = np.genfromtxt(   StringIO(text.read()), 
                            delimiter=",", ## 定义分隔符
                            dtype = "float") ## 定义数据类型
    
''' 计算统计信息 '''
stat = np.array( [data.mean(axis = 0), ## 统计每一列的 均值
                  data.var(axis = 0), ## 方差
                  data.std(axis = 0)] ) ## 标准方差

''' 结束以后，打开screen.txt看看结果吧 '''
np.savetxt('screen.txt', stat, delimiter = '\t', fmt = '%.2f') ## 把结果存入screen.txt文件，
                                                               ## 这样可以避免看科学计数格式
print stat