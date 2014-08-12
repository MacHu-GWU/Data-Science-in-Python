##coding=utf8
##By, Sanhe
import numpy as np
from sklearn.preprocessing import Imputer
import scipy.sparse as sp

''' example 1 针对numpy普通矩阵 '''
# X = [[1, 2], 
#      [np.nan, 3], 
#      [7, 6]]
# imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
# imp.fit(X)
# 
# X = [[np.nan, 2], 
#      [6, np.nan], 
#      [7, 6]]
# print imp.transform(X)

# ## sklearn.preprocessing.Imputer 中内置了3种模式自动填补空缺的值。其中没有knn方法
# If “mean”, then replace missing values using the mean along the axis.
# If “median”, then replace missing values using the median along the axis.
# If “most_frequent”, then replace missing using the most frequent value along the axis.
''' example 2 针对稀疏矩阵 '''
# X = sp.csc_matrix([[1, 2], 
#                    [0, 3], 
#                    [7, 6]])
# 
# imp = Imputer(missing_values=0, strategy='mean', axis=0)
# imp.fit(X)
# 
# X_test = sp.csc_matrix([[0, 2], 
#                         [6, 0], 
#                         [7, 6]])
# print(imp.transform(X_test))
