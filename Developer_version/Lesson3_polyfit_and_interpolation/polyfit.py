##coding=utf8
##By, Sanhe
import numpy as np
import matplotlib.pyplot as plt
## [标题]如何用Python做曲线拟合，多项式分析

''' 1. 根据多项式系数求 f(x) 的值 '''
# a = [1,0,0] ## y = 1*x^2 + 0*x + 0
# p = np.poly1d(a) ## 建立 poly1d 对象
# print p(0.1), p(0.2), p(0.3) ## 对单个x值求值
# xp = [1,2,3] ## 对多个x值向量求多项式值
# print p(xp)

''' 2. 根据样本值拟合多项式系数 '''
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
a3 = np.polyfit(x, y, 3) ## 3阶拟合，即x最高次方系数是3
a10 = np.polyfit(x, y, 10) ## 10阶拟合，即x最高次方系数是10
p3 = np.poly1d(a3)
p10 = np.poly1d(a10)
## 画图验证
xp = np.linspace(0,5,10)
plt.plot(x, y, '.', markersize = 10)
plt.plot(xp, p3(xp), 'r--')
plt.plot(xp, p10(xp), 'b--')
plt.show()

# 更多信息请参考官方文档: http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html