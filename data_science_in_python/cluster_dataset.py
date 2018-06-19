#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

import matplotlib
matplotlib.use('TkAgg')


n_samples = 1500
X, y = datasets.make_circles(
    n_samples=n_samples,
    factor=.5, noise=.05,
)


# plt.scatter(X)
