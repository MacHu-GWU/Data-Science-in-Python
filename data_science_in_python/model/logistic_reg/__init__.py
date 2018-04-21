# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
# License: BSD 3 clause

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import datasets
from sklearn.svm import l1_min_c

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 2]
y = y[y != 2]

X -= np.mean(X, 0)

# #############################################################################
# Demo path functions
cs = l1_min_c(X, y, loss='log') * np.logspace(0, 3, num=50)
print(np.logspace(0, 3, 50))
print(cs)

# print("Computing regularization path ...")
# start = datetime.now()
# clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
# coefs_ = []
# for c in cs:
#     clf.set_params(C=c)
#     clf.fit(X, y)
#     coefs_.append(clf.coef_.ravel().copy())
# print("This took ", datetime.now() - start)
#
# coefs_ = np.array(coefs_)
# plt.plot(np.log10(cs), coefs_)
# ymin, ymax = plt.ylim()
# plt.xlabel('log(C)')
# plt.ylabel('Coefficients')
# plt.title('Logistic Regression Path')
# plt.axis('tight')
# plt.show()