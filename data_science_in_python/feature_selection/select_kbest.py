#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

For regression:

- f_regression
- mutual_info_regression

For classification:

- chi2
- f_classif
- mutual_info_classif
"""
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

iris = load_iris()
X, y = iris.data, iris.target
X_new = SelectKBest(score_func=chi2, k=2).fit_transform(X, y)
# print(X_new.shape)
print(X, y)
print(chi2(X, y))