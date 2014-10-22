##encoding=utf8
##version =py27, py33
##author  =sanhe
##date    =2014-10-16

"""
对于线性可分的数据集，感知器分类器的实现
"""
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import copy

def predict(sample, weight):
    """根据感知器的权值预测一个样本的类标
    """
    sample = copy.copy(sample)
    try:
        if type(sample) == list:
            sample.append(1)
        else:
            sample = list(sample)
            sample.append(1)
        total = np.inner(np.array(sample),
                         np.array(weight) )
        if total > 0:
            return 1
        else:
            return 0
    except:
        raise Exception("Sample is:\n%s\nPlease validate the sample." % sample)        

data = [([1, 3], 1), # 每个tuple是一个样本，第一个元素是数据，第二个元素是类标
        ([2, 5], 1),
        ([-1, 4], 0),
        ([-2, 1.5], 0)]

weight, e = np.array([1, -1, 0]), 0.1

while 1:
    flag = 1
    for s, label in data:
        output = predict(s, weight)
        if output != label:
            weight = weight + e * (label - output)
            flag = 0
            break
    if flag:
        break
    
for s, label in data:
    print(predict(s, weight), label)

