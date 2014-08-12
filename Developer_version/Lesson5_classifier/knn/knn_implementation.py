##coding=utf8
'''
This example is to teach the basic knn neighboor search algorithm implementation
in python - sklearn.neighbors

In this example, you can understand once given a training data-set, having any
test sample, how to quickly get the k-neighboors and the distances.
'''

''' EXAMPLE1
Performance test - KNN search algorithms: ball_tree & kd_tree
This is a demo to compare the speed of these two algorithms. Usually, kd_tree
has better performance.
'''
def example1():
    import numpy as np
    from sklearn.neighbors import NearestNeighbors
    import time
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    ''' ball_tree algorithm '''
    st = time.clock()
    ## create a neighboors object. apply NearestNeighbors.fit(data) method 
    nbrs1 = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
    print '\nnbrs1.kneighbors(X): \n', nbrs1.kneighbors(X) ## returns tuple(distance, index)
    print '\nball_tree cost seconds: \n', time.clock() - st ## calculate time consuminig
    
    ''' kd_tree algorithm '''
    st = time.clock()
    nbrs2 = NearestNeighbors(n_neighbors=2, algorithm='kd_tree').fit(X)
    print '\nnbrs2.kneighbors(X): \n', nbrs2.kneighbors(X)
    print '\nkd_tree cost seconds: \n', time.clock() - st

# example1()

''' EXAMPLE2
This examples shows for each samples in test data-set, find the first K nearest
neighboors in train data-set
'''
def example2():
    import numpy as np
    from sklearn.neighbors import NearestNeighbors
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(X)
    distances, indices = nbrs.kneighbors([[0,0], [1,1]]) ## nbrs.kneighbors(X), X
    ## is the test data set. In this case, it find the first nearest neighboor of [0,0] and [1,1]
    print '\nindices: \n', indices

# example2()

''' EXAMPLE3
This examples demonstrate an ordinary KNN classifier application in
classification task.
'''
# test data, copd_1000.txt explaination.
# 1. age                  int
# 2. gender               int 0/1 = female/male
# 3. years of smoking     int
# 4. cigarette per day    int
# 5. FEV% average         float
# 6. FEV% today           float
# 7. Oxygen Saturation%   float
# 8. Walking miles perday float
# 9. COPD level           int [Label], given new data with features 1-7, find the COPD level

def example3():
    ### --- load train data --- ###
    import numpy as np
    import pandas as pd
    from StringIO import StringIO
    from sklearn import preprocessing    
    from sklearn.neighbors import NearestNeighbors
    with open('copd_1000.txt', 'rb') as text:
        data = np.genfromtxt(   StringIO(text.read()), 
                                delimiter=",", ## define the delimiter
                                dtype = float) ## define datatype


    ### --- standardize train data, remove mean and var --- ###
    df = pd.DataFrame(data)
    df = df[[0,2,3,4,5,6,7]] ## eliminate the second feature: AGE
    scaler = preprocessing.StandardScaler().fit(df)
    m = scaler.mean_ ## mean
    std = scaler.std_ ## std
    train = scaler.transform(df) ## standardize
    ### --- standardize test data, using same mean and var in train data --- ###
    test = np.array([[81, 0, 66, 8, 0.71, 0.67, 0.87, 1.61],
                     [75, 1, 53, 7, 0.95, 0.92, 0.98, 1.49]]) ## there's no label
    test = pd.DataFrame(test)
    test = test[[0,2,3,4,5,6,7]] ## eliminate the second feature: AGE
    test = scaler.transform(test)
    ### --- KNN neighboor search --- ###
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(train)
    distances, indices = nbrs.kneighbors(test)
    print distances
    print indices ## indices = [[79], [71]] 
                  ## which means the data[79] is the nearest data for test[0]
    ### --- get the classification prediction --- ###
    print data[indices].transpose()[-1] ## data[indices] get the nearest neighboor
                                        ## transpose() get the transpose
                                        ## [-1] get the last column, which is the label

example3()
