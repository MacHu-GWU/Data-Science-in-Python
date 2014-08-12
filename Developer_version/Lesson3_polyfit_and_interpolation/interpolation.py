##coding=utf8
##By, Sanhe
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
## [标题]如何用Python做曲线拟合，多项式分析

''' 1. Numpy 方法 '''
''' 对一个点进行差值 '''
# x = [1,2,3]
# y = [3,2,0]
# print np.interp(2.5, x, y)

''' 对一个向量进行插值 '''
# x = [1,2,3,4,5,6,7]
# y = [11.9,   24.6,   45.3,   73.9,  108.2,  151.1,  202.3]
# # ## 下面的y其实是有2阶多项式生成后加噪声形成的
# # a = [3.7, 2.1, 5.8]
# # p2 = np.poly1d(a)
# # y = p2(x)
# x1 = np.linspace(1,7,100)
# y1 = np.interp(x1, x, y)
# 
# plt.plot(x,y, 'o')
# plt.plot(x1,y1, '^')
# plt.show()
# 
# print y1 ## 打印差值后的y值
# print np.diff(y1) ## 打印y的差分，可以发现numpy中的差值是均值差值，效果并不好

''' 2. Spicy 方法 , cubic spline 差值'''
# x = np.linspace(0, 10, 10)
# y = np.cos(-x**2/8.0)
# f = interp1d(x, y) ## 均值差值 差值器
# f2 = interp1d(x, y, kind='cubic') ## cubic 差值器
# xnew = np.linspace(0, 10, 40)
# 
# ## 画图验证
# plt.plot(x,y,'o',xnew,f(xnew),'g-', xnew, f2(xnew),'r--')
# plt.legend(['data', 'linear', 'cubic'], loc='best')
# plt.show()