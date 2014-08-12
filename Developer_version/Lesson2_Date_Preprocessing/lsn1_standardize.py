##coding=utf8
##By, Sanhe
from sklearn import preprocessing
import numpy as np
'''
注意！sklearn中的数据预处理是按照
每行是一个样本
每列是一种特征
'''
X = np.array([[1,2,3], ## dtype = 'f' 非常重要，为了标准化，矩阵元素必须是浮点类型
              [3,5,7],
              [5,8,11]], dtype = 'f')

''' 简单直接标准化，去均值和方差 '''
# X_scale = preprocessing.scale(X)
# print X_scale
# print X_scale.mean(axis = 0) ## 按列求均值,跟matlab一致
# print X_scale.mean(axis = 1) ## 按行求均值

''' 标准化的同时，储存均值和方差，以供之后使用  [推荐]'''
# scaler = preprocessing.StandardScaler().fit(X)
# print scaler.transform(X)
# print scaler.mean_ ## 返回每列的均值
# print scaler.std_ ## 返回每列的标准差

''' 二值化 Binarization '''
# binarizer = preprocessing.Binarizer(threshold = 3.1) ## 低于threshold的都会被判为0
# print binarizer.transform(X)

''' 把样本线型压缩到某个区间内 ,s实际上是
x_minmax = ( x - min(x) ) / max( x - min(x) )
'''
# min_max_scaler = preprocessing.MinMaxScaler()
# X_minmax = min_max_scaler.fit_transform(X)
# print X_minmax

''' Label binarization 二值化 '''
# lb = preprocessing.LabelBinarizer()
# lb.fit([1, 2, 6, 4, 2])
# print lb.classes_
# print lb.transform([(1,2),(1,2)])

''' Label encoding 重新命名类标，从0开始编号 '''
# le = preprocessing.LabelEncoder() ## 创建LabelEncoder对象
# le.fit([6, 2, 2, 1]) ## 训练le对象，实际上是把 [1,2,6] 映射到 [0,1,2]
# print le.classes_ ## 原始类标中是排序过了的
# print le.transform([6]) ## 对于6，是第三个类标，所以新类标是2
# print le.inverse_transform([2]) ## 对于新类标2，反映射到原始类标则是6

imp = preprocessing.imputation.Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], 
         [np.nan, 3], 
         [7, 6]])



# X_normalized = preprocessing.normalize(X, norm = 'l2')
# import numpy.linalg as npl
# print npl.norm( X_normalized )