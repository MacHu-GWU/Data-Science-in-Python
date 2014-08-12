##coding=utf8
import numpy as np
import numpy.linalg as npl
from sklearn import linear_model
## y = x * b
b = np.array([3,5,7]).transpose()
x = np.array([[1,6,9],   ## 1*3 + 6*5 + 7*9 = 96
              [2,7,7],   ## 2*3 + 7*5 + 7*7 = 90
              [3,4,5],   ## 3*3 + 4*5 + 5*7 = 64
              [6,3,8]])  ## 6*3 + 3*3 + 8*7 = 89
print np.dot(x,b)
y = np.array([96,90,64,89]).transpose()

clf = linear_model.LinearRegression(fit_intercept=False)
# clf.fit (x, y.transpose())
clf.fit([[1,6,9],
         [2,7,7],
         [3,4,5],
         [6,3,8]], [95,91,62,89.5])
print clf.coef_
print np.dot(x, clf.coef_)


# 0 0     0
# 1 1     1
# 2 2     2

# b = np.array([0.5,0.8]).transpose()
# x = np.array([[0,0],
#               [1,1],
#               [2,2]])
# print np.dot(x,b) ## [0, 1.3, 2.6]
# 
# y = np.array([0, 1.3, 2.6]).transpose()
# clf = linear_model.LinearRegression()
# clf.fit (x, y)
# print clf.coef_
# print np.dot(x, clf.coef_) ## []]