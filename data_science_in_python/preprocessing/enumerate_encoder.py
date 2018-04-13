#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Replace item collection array into enumerate integer.
"""

import pandas as pd

X = pd.DataFrame([["male",   "US",       "Chrome"],
                  ["male",   "Asian",    "FireFox"],
                  ["female", "Europe",   "Safari"],
                  ["male",   "US",       "IE"]])
"""
transform to::

        0   1   2
    0   1   2   0
    1   1   0   1
    2   0   1   3
    3   1   2   2
"""

def enumerate_encoder(array, sorted_labels=None):
    if sorted_labels is None:
        sorted_labels = list(set(array))
        sorted_labels.sort()
    mapper = {item: i for i, item in enumerate(sorted_labels)}
    return [mapper[item] for item in array]

for c in X.columns:
    X[c] = enumerate_encoder(X[c])
