##coding=utf8
''' EAXMPLE1
用KNN查找法，填充每一个数据缺失值。方法如下：
如果有一个数据缺失值在第10行3列。
    1. 看第10行，是否还有其他缺失值，如果有，这些缺失值所在的列(cbadind)都不能出现在训练集中
    2. 遍历其他的缺失值的坐标，如果其列坐标 不在cbadind中，或者等于第3列，则这些缺失值的行
    坐标都不能出现在训练集中
    3. 生成训练集，并且用knn找到有缺失值的那行数据的最近邻。并记录行号
    4. 根据行号找到近邻，其第3列的值就可以用来填充了
代码如下
'''
def example1():
    ### --- load data --- ###
    import numpy as np
    import pandas as pd
    from StringIO import StringIO
    from sklearn import preprocessing    
    from sklearn.neighbors import NearestNeighbors
    ### 函数功能: 给定一个NaN的索引，找到knn填充算法所需要的训练集 ###    
    def find_helpful_train(index, column, nancordlist, thecord):
        rbadind, cbadind = list(), list()
        ## 1.首先跟thecord同一行的nan所在的所有列是不能要的
        for cord in nancordlist:
            if cord[0] == thecord[0]:
                cbadind.append(cord[1])
        cbadind = set(cbadind)
        ## 2.其次遍历所有的NaN元素 ##
        for cord in nancordlist: ## 当NaN元素的列标号 不在cbadind.difference({thecord[1]}中时
            if cord[1] not in cbadind.difference({thecord[1]}): ## 说明这个NaN元素所在的行不能用
                rbadind.append(cord[0])
        rbadind.append(thecord[0])
        rbadind = set(rbadind)
        ## 3.把不能要的用set.difference剔除， cbadind在找到测试集合的时候有用
        return list(index.difference(rbadind)), list(column.difference(cbadind)), cbadind
    ## START! ##
    with open('copd_1000_with_missing_value.txt', 'rb') as text:
        data = np.genfromtxt(   StringIO(text.read()), 
                                delimiter=",", ## define the delimiter
                                dtype = float) ## define datatype
    data = pd.DataFrame(data)
#     print data[0:10] ## <== as you can see there are some missing value
#                      ## in 6,7,8th row
    rindex, cindex = np.where(np.isnan(data) == True) ## NaN value's row, column index
    nancordlist = zip(rindex, cindex) ## zip NaN value coordinate pairs
    index, column = set(data.index), set(data.columns)
    res = dict()
    ## for all NaN point, find the predict value ##
    for thecord in nancordlist:
        rr, cc, cbadind = find_helpful_train(index, column, ## rr是可用来knn插值法的rowindex
                                    nancordlist, thecord) ## cc是可用来knn插值法的columnindex
        train = data.loc[rr, cc] ## 取出训练集
        test = data.loc[thecord[0], ## 取出测试集
                       list(column.difference(cbadind))]
        ## a. Standardization
        scaler = preprocessing.StandardScaler().fit(train)
        stdtrain = scaler.transform(train) ## standardize train
        stdtest = scaler.transform(test) ## standardize test
        ## b. Knn find the nearest neighboor's index
        nbrs = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(stdtrain)
        dist, nb_ind = nbrs.kneighbors(stdtest)
        ## c. find the corresponding value by the 1NN row number
        ## nb_ind[0][0]是rr中的标号，原始数据所在的实际行标号实际上是rr[nb_ind[0][0]]
        res[thecord] = data.loc[ [rr[nb_ind[0][0]]], [thecord[1]] ].values[0][0] ## 记录thecord所在的NaN所填充的缺失值
    ## impute data ##
    for cord, value in res.items(): ## 对每个缺失值所在的位置的值进行填充
        data.loc[[cord[0]],[cord[1]]] = value
    np.savetxt('copd_1000_fixed.txt', data.values, fmt = '%s', delimiter = ',') ##保存为文件

example1()
