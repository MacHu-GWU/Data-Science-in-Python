##coding=utf8
## 注意！！ Numpy矩阵是一个以行向量为导向的矩阵
import numpy as np
''' === 建立矩阵  === '''
data1 = np.array([[ 0.9526, -0.246 , -0.8856],
                  [ 0.5639, 0.2379, 0.9104]])
print 'data1为:\n%s\n' % data1

''' === 矩阵转置  ==='''
# print np.transpose(data1)

''' === 取得元素，行，列  === '''
# print data1[0] ## 取第1行
# print data1[1] ## 取第2行
# print data1[(0,1)] ## 取 第1行 第2个元素
'''
    Numpy中不存在列向量的概念，要想取得列向量
        只能用如下技巧
'''
# print np.transpose(data1)[1]

''' === 建立等差数列  === '''
# data2 = np.linspace(1,10,10) ## (a,b,num) 从a到b，共10个元素
# print data2
# print data2[0]

''' === 建立基本 0矩阵 1矩阵 对角矩阵 === '''
# print np.zeros((2,3))
# print np.ones((2,3))
# print np.eye(2,3)

# print np.ones_like([[1,2,3],[4,5,6]]) ## 生成跟 np.ones_like(array) 大小一样的矩阵

''' === 取得矩阵大小 === '''
# print data1.shape

''' === 改变矩阵形状  === '''
# print data1.reshape(3,2)

''' 1. 改变大小 '''
# print '矩阵之前是:\n', data1
# print '正在用reshape改变矩阵:\n', data1.reshape((3,2)) ## 注意！此方法不会改变矩阵本身
# print '矩阵reshape之后是,并无变化:\n', data1
# data1.resize((3,2)) ## 注意！此方法会改变矩阵本身
# print '矩阵resize之后是:\n', data1

''' 2. 变为向量 '''
# print data1.flatten() ## 将矩阵压平

''' 3. 变换数据类型  '''
# print data1.astype('int') ## 数据类型可以参考 http://docs.scipy.org/doc/numpy/user/basics.types.html

''' === 矩阵内部元素运算 === '''
# ## 所有的方法都是针对全部的元素，而不像matlab中的列向量
# print data1.max() ## 最大值
# print data1.min() ## 最小值
# print data1.sum() ## 求和
# print data1.cumsum() ## 累积和
# print data1.prod() ## 积
# print data1.cumprod() ## 累计积
# print data1.all() ## 如果所有元素为真，则返回真，否则返回假
# print data1.any() ## 只要有一个元素为真则返回真
# print data1.mean() ## 求均值
# print np.unique(np.array([[1,1,2,2,3,3],        ## 求distinct value
#                           [2,2,3,3,4,4]])    )

''' === 切片操作  === '''
# data2 = np.array([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
# print 'data2为:\n%s\n' % data2

''' 1. 根据坐标 取得元素 '''
# print data2[1,2]
# print data2[(1,2)]

''' 2. 取得行  '''
# print data2[0]

''' 3. 取得列 '''
# print data2.transpose()[0]

''' 根据简单index切片 '''
# index = [0,1]
# print data2[index]  ## 取得行
# print data2.transpose()[index] ## 取得列

''' 根据复杂index切片 '''
# x = np.random.randn(10,10)
# b = x > 0.1
# print x[b]

''' === 统计函数  === '''
''' === 向量对象 === '''
# ## 定义SUM符号表示 SUM = (x1-u)^2 + (x2-u)^2 + ...
# data3 = np.array([-1,0,1])
# print '数据: %s' % data3
# print '均值: %s' % data3.mean() ## 均值
# print '方差: %s' % data3.var() ## 方差 def: SUM / N
# print '整体标准差: %s' % data3.std() ## 整体标准差 def: (SUM / N) ^ 2
# ##
# data3 = np.array([1,2,4,5,6,8,9])
# print np.average(data, weights = [1,2,3,4,5,6,7]) ## 加权平均
# print np.median(data) ## 中位数

''' === 矩阵对象 === '''
# data3 = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])
# print data3.mean(axis = 0, ## 0 = 按列求平均, 1 = 按行求平均
#                  keepdims = 1), '均值' ## keepdims = 0 输出1纬向量, = 1输出2纬矩阵
# print data3.var(axis = 0, ## 0 = 按列求平均, 1 = 按行求平均
#                  keepdims = 1), '方差' ## 输出2纬向量
# print data3.std(axis = 0, ## 0 = 按列求平均, 1 = 按行求平均
#                  keepdims = 1), '标准差' ## 输出2纬向量
