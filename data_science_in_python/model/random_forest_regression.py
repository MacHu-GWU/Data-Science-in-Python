#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

def f(x):
    return 0.5 * np.exp(-(x+3)**2) + np.exp(-x**2) + 0.5 * np.exp(-(x-3)**2)

N = 200 # 200 samples

x_train = np.linspace(-5.5, 5.5, N)
X_train = pd.DataFrame({"x": x_train})
y_train = f(x_train) + (np.random.rand(N) - 0.5) * (2 * 0.05)

dtr = DecisionTreeRegressor(max_depth=5)
br = BaggingRegressor(dtr, n_estimators=200, max_samples=0.2)
br.fit(X_train, y_train)

x_test = np.linspace(x_train.min() * 1.1, x_train.max() * 1.1, 1000)
X_test = pd.DataFrame({"x": x_test})
y_test = f(x_test)
y_predict = br.predict(X_test)

plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test)
plt.scatter(x_test, y_predict)
plt.show()
