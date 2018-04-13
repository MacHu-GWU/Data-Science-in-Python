#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import preprocessing

X = pd.DataFrame([[0, 0, 3],
                  [1, 1, 0],
                  [0, 2, 1],
                  [1, 0, 2]])

enc = preprocessing.OneHotEncoder()
enc.fit(X)

print(enc.n_values_)
print(enc.feature_indices_)

y = [[0, 1, 3]]
# print(enc.transform(y))

# print(enc.transform([[0, 1, 3]]).toarray())
