##coding=utf8
##author=Sanhe
##date=07-13-2014

import numpy as np

def problem1(m,n):
    data = np.linspace(1,m*n,m*n) ## generate 1 --- m*n
    data = data.reshape(m,n) ## reshape the vector to a matrix
    return data

def problem2(n):
    data = np.ones((n,n))
    for i in range(1,n):
        for j in range(1,n):
            if i+j >= n: ## lower triangle should be all zeros
                data[(i,j)] = 0
            else: ## calculate elements by definition
                data[(i,j)] = data[(i, j-1)] + data[(i-1, j)]
    return data
    
if __name__ == '__main__':
    print '\nProblem1 Result:\n%s' % problem1(5,6)
    print '\nProblem2 Result:\n%s' % problem2(10)