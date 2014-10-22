##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-15

"""
[标题]如何用Python做曲线拟合，多项式分析
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def example1():
    """ 1. 根据多项式系数求 f(x) 的值 
    np.poly1d(a) 根据系数a 生成一个多项式计算器
    np.poly1d(a)(x) = f(x) 其中 f(x)是以a为系数的多项式
    """
    a = [1,0,0] ## y = 1*x^2 + 0*x + 0
    p = np.poly1d(a) ## 建立 poly1d 对象
    print(p(0.1), p(0.2), p(0.3) ) ## 对单个x值求值
    xp = [1,2,3] ## 对多个x值向量求多项式值
    print(p(xp) )

example1()

def example2():
    """ 2. 根据样本值拟合多项式系数 
    np.polyfit(x_data, y_data, p) 根据 x, y数据和阶数p返回拟合的多项式系数列表
    """
    x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
    y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
    a3 = np.polyfit(x, y, 3) ## 3阶拟合，即x最高次方系数是3
    a10 = np.polyfit(x, y, 10) ## 10阶拟合，即x最高次方系数是10
    p3 = np.poly1d(a3)
    p10 = np.poly1d(a10)
    ## 画图验证
    xp = np.linspace(0,5,10)
    plt.plot(x, y, ".", markersize = 10) # 点是原数据
    plt.plot(xp, p3(xp), "r--") # 红线是3阶拟合
    plt.plot(xp, p10(xp), "b--") # 蓝线是10阶拟合
    plt.show()

example2()
# 更多信息请参考官方文档: http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html