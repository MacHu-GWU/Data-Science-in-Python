import numpy as np
from sklearn.linear_model import SGDClassifier

X = np.array([[1, 3],
              [2, 5],
              [-1, 4],
              [-2, 1.5]])
Y = np.array([0, 1, 1, 0])
clf = SGDClassifier().fit(X, Y)

print(clf.predict([1, 3]) )