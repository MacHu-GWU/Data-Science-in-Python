##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-15

from __future__ import print_function
import numpy as np
import numpy.linalg as npl
from sklearn import linear_model

def example1():
    """测试数据
    y = x * b
    """
    b = np.array([3,5,7]).transpose()
    x = np.array([[1,6,9],   ## 1*3 + 6*5 + 7*9 = 96
                  [2,7,7],   ## 2*3 + 7*5 + 7*7 = 90
                  [3,4,5],   ## 3*3 + 4*5 + 5*7 = 64
                  [6,3,8]])  ## 6*3 + 3*3 + 8*7 = 89
    y = np.array([96,90,64,89]).transpose()
    
    clf = linear_model.LinearRegression(fit_intercept=False)
    clf.fit([[1,6,9],
             [2,7,7],
             [3,4,5],
             [6,3,8]], [95, 91, 62, 89.5]) # 改变一点点y的值
    print( clf.coef_ ) # 所以解出来的b值也差别不大
    print( np.dot(x, clf.coef_) ) # 验证结果

example1()