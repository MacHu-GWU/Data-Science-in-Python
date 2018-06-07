#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from dateutil.parser import parse
from collections import OrderedDict

# Time Stamp
y1980_ts_sec = (datetime(1980, 1, 1) - datetime(1970, 1, 1)).total_seconds()
y2030_ts_sec = (datetime(2030, 1, 1) - datetime(1970, 1, 1)).total_seconds()
y1980_ts_ms = y1980_ts_sec * 1000
y2030_ts_ms = y2030_ts_sec * 1000

epoch = datetime(1970, 1, 1)


class FeaturePreprocessor(object):
    def __init__(self):
        self.numeric_columns = list()
        self.category_columns = list()
        self.datetime_columns = list()
        self.boolean_columns = list()

        self.cardinality_matrix = OrderedDict()

    def fit(self, df, one_hot_encoding=True):
        self.__init__()

        n_row, n_column = df.shape

        for column in df.columns:
            series = df[column]
            n_unique = len(series.unique())

            # find cardinality
            cardinality = n_unique / n_row
            self.cardinality_matrix[column] = cardinality

            # find datetime type
            # check string type
            first_notnull_value = series[series.notnull()].head(1).values[0]
            try:
                parse(first_notnull_value)
                df[column] = series.apply(self._parse_datetime_from_str)
                self.datetime_columns.append(column)
            except:
                pass

            # check numeric type
            describe = series.describe()
            try:
                median_value = describe["50%"]
                if y1980_ts_sec <= median_value <= y2030_ts_sec:
                    df[column] = series.apply(self._parse_datetime_from_second)
                    self.datetime_columns.append(column)
                elif y1980_ts_ms <= median_value <= y2030_ts_ms:
                    df[column] = (series / 1000).apply(self._parse_datetime_from_second)
                    self.datetime_columns.append(column)
            except:
                pass

        # find category type
        for column, cardinality in self.cardinality_matrix.items():
            if cardinality <= 0.01:
                if one_hot_encoding:
                    self.one_hot_encoding(df, column)

    def one_hot_encoding(self, df, column):
        series = df[column]
        unique_values = series[series.notnull()].unique()
        for value in unique_values:
            key = "%s_%s" % (column, value)
            df[key] = series == value
        return df

    def _parse_datetime_from_str(self, value):
        try:
            return parse(value)
        except:
            return None

    def _parse_datetime_from_second(self, value):
        try:
            return epoch + timedelta(seconds=value)
        except:
            return None


from sklearn import datasets


# boston_data = datasets.load_boston()
# X = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
# y = boston_data.target

class Feature:
    f01_numeric = None
    f02_cate = None
    f03_time = None
    f04_time = None
    f05_time = None


columns = list()
for attr, _ in Feature.__dict__.items():
    if not attr.startswith("__"):
        setattr(Feature, attr, attr)
        columns.append(attr)
columns.sort()

n_rows = 1000
n_columns = len(columns)

data = {
    Feature.f01_numeric: np.random.randn(n_rows),
    Feature.f02_cate: np.random.randint(1, 3, n_rows),
    Feature.f03_time: np.random.randint(1483228800, 1514764800, n_rows),
    Feature.f04_time: np.random.randint(1483228800000, 1514764800000, n_rows),
    Feature.f05_time: ["2015-01-01", ] * n_rows,
}
df = pd.DataFrame(data, columns=columns)

na_ratio = 0.05


def assign_random_na(df, na_ratio):
    na_count = int(na_ratio * df.shape[0] * df.shape[1])
    for _ in range(na_count):
        row_ind = np.random.choice(df.index)
        col_ind = np.random.choice(df.columns)
        df.loc[row_ind, col_ind] = None
    return df


df = assign_random_na(df, na_ratio=na_ratio)

fp = FeaturePreprocessor()
fp.fit(df)
print(df.head(5))
