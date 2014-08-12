##coding=utf8
# 在数据分析的时候，很多时候每一列的的值有不同的数据类型。
# 而根据某一列的值进行排序是非常常见的，本文档的内容就是
# 为了解决这一矩阵排序问题。
import numpy as np
''' 情况1： 简单的按某一列排序 '''
# 每一个样本数据必须要用元组的形式，而不是列表的形式储存（据
# 说是为了符合python里面的buffer type），而dtype中必须定义
# 列名称，和每列的数据类型。数据类型的格式如下：
# dtype = [('columnname1', 'dtype1'),
#          ('columnname2', 'dtype2'),
#          ('columnname3', 'dtype3')]
# numpy.array(data, dtype) 中dtype所支持的格式如下:
# [ref]: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
# 
# 'b'    Boolean
# 'i'    (signed) integer
# 'u'    unsigned integer
# 'f'    floating-point
# 'c'    complex-floating point
# 'S', 'a'    string
# 'U'    unicode
# 'V'    raw data (void)
''' 例子 '''
data = np.array([(int(3), float(1.2), 'Tb'), ## 一定要用元组储存数据
                 (int(1), float(4.5), 'Ta')], 
                dtype = [('x', int),('y', float),('z', 'S2')])
data.sort(order = 'z')
print data
''' 情况2: 与数据库中排序类似，按照优先级，根据多列进行排序 '''
# 比如首先根据第一列排序，如果第一列内容相等，则再根据第二列内容调整顺序
# 但是，python numpy并不支持逆序排序
''' 例子 '''
# data = np.array([(1,3,'a'),
#                  (1,2,'b'),
#                  (2,1,'c')],
#                  dtype = [('x', int),('y', int),('z', 'S1')])
# data.sort(order = ['x', 'y']) ## 首先按照第一列排序，第一列相同的情况下按第二列排序
# print data