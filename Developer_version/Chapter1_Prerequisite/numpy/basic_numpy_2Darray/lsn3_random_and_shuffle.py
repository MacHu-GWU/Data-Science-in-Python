##coding=utf8
##By. Sanhe 2014-06-09
# 用numpy生成随机数
import numpy as np
''' === Simple random data  === '''
# print np.random.randn(3,3) ## N(0,1) distribution
# print np.random.rand(3,3) ## U(0,1) distribution
# print np.random.randint(1, 5, size = 100) ## in range(#low, #high) generate #size samples
# print np.random.choice(a = [11,12,13,14,15], ## 从一个数组中选出size个数据，根据p中的离散概率分布
#                        size = 3, ## a:数据源, size:选出多少个, p:概率分布
#                        p=[0.1, 0, 0.3, 0.6, 0])

''' === Permutations  === '''
# arr = np.arange(10)
# np.random.shuffle(arr) ## shuffle方法会改变arr本身
# print arr
# print np.random.permutation(10) ## = randperm(10) in matlab

''' === Distribution === '''
print np.random.beta(1,2,size = (2,5))