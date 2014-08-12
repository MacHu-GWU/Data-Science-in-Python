##coding=utf8
##By. Sanhe 2014-06-09
# [标题] 如何把数据保存为txt或csv文件
# 在数据IO中,由于作为一般的数据储存媒介 --- 文本，数据都是以字符串的形式储存的。
# 所以如何将复杂数据字符串化，以及从字符串中读取并转化成相应的数据类型就显得非常
# 重要。numpy支持的常用数据类型有: int, float, bool, string。
# ==================================================================
# 简单情况下，整个文件中的数据都是一类格式。
# 复杂情况下，每一列的数据格式很可能大不相同。
# 本文档介绍了如何在各种情况下读写数据。

import numpy as np
fname1 = 'dump_data1.txt' ## 如果要存成csv，只需要改变扩展名为csv即可
fname2 = 'dump_data2.txt' ## 如果要存成csv，只需要改变扩展名为csv即可
fname3 = 'dump_data3.txt' ## 如果要存成csv，只需要改变扩展名为csv即可
''' 1. 本例中，数字的精度被改变成小数点后保留2位'''
data1 = np.array([[1.111,2.222,3.333],
                 [4.444,5.555,6.666],
                 [7.777,8.888,9.999]])
np.savetxt(fname1, ## 文件名
           data1,  ## 数据
           fmt= ['%.2f', '%i', '%s'], ## 定义格式， fmt = format  %.2f = 小数点后保留2位
           delimiter = ',', ## 定义分隔符
           header = 'one, two, three') ## 定义表头

''' 2. 本例中，数字都被当成字符串储存了 '''
data2 = np.array([[1.111,2.222,'three'],
                 [4.444,5.555,'six'],
                 [7.777,8.888,'nine']])
np.savetxt(fname2, data2, fmt = '%s', delimiter = ',') ## %s 保存为字符串

''' 3. 本例中，每列的数据类型被分别定义了 '''
data3 = np.array([(1.111,2.222,'three'), # [Watch out! Sample has to be tuple]
                  (4.444,5.555,'six'),
                  (7.777,8.888,'nine'), ],
                 dtype = [('x', int),('y', float),('z', 'S5')]) ## 一定需要预定义和
np.savetxt(fname3, data3, 
           fmt= ['%d', '%.2f', '%s'], ## 第一列是整数，第二列是小数点保留两位浮点，第三列是字符串 
           delimiter = ',',
           header = 'one, two, three')
# 更多资料请参考
# numpy.savetxt介绍: http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html