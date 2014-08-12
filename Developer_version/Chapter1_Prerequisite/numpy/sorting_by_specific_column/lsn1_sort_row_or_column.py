##coding=utf8
# 在数据分析的时候，很多时候会想要把矩阵中的每一行，或者每一列独立的各自排序。
# 本文档内容就是为了解决这一问题的。
# [ref]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html
import numpy as np
a = np.array([[1,3,7],
              [3,1,5],
              [2,6,8]])

''' 所有元素排序，并且压平到向量 '''
# print np.sort(a, axis = None) ## 
# res = np.sort(a, axis = None)
# print res[::-1] ## [重要技巧！]逆序输出结果

''' 按列排序，即每列中的元素，内部进行排序 '''
# print np.sort(a, axis = 0)
# res = np.sort(a, axis = 0)
# print res[::-1] ## [重要技巧！]逆序输出结果

''' 按行排序, 即每行中的元素，内部进行排序 '''
# print np.sort(a, axis = 1)
# res = np.sort(a, axis = 1)
# print res.transpose()[::-1].transpose() ## [重要技巧！]逆序输出结果