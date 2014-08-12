##coding=utf8
##author=Sanhe
##date=07-13-2014

import numpy as np

'''
=== PROBLEM 01 ===
create a m*n matrix, start from 1, end with m*n
for example m, n = 2, 3
data = [[1,2,3],
        [4,5,6]]
'''

def problem1(m,n): ## <=== INSERT YOUR CODES HERE
    ''' Hint: use linspace and reshape '''
    
    
    return data
    
'''
=== PROBLEM 02 ===
create a n*n Pascal's triangle, upper triangular matrix
you can find the definition here: http://en.wikipedia.org/wiki/Pascal's_triangle
for example if n = 4, the matrix should looks like:

[[1, 1, 1, 1],
 [1, 2, 3, 0],
 [1, 3, 0, 0],
 [1, 0, 0, 0]]
'''
    
def problem2(n): ## <=== INSERT YOUR CODES HERE
    ''' Hint: apply the definition '''
    return data


if __name__ == '__main__':
    print '\nProblem1 Result:\n%s' % problem1(5,6)
    print '\nProblem2 Result:\n%s' % problem2(10)