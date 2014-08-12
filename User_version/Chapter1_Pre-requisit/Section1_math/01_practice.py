##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
In mathematics, a combination is a way of selecting members from a grouping, 
such that (unlike permutations) the order of selection does not matter.

you can find the formula here: http://en.wikipedia.org/wiki/Combination

for example,  c(5,2) is the number of different ways to select 2 items from
5 items, which is 10.
'''

'''
=== PROBLEM 01 ===
In this exercise, please write the function to calculate c(n, k), which means
number of ways to choose k from n items.
'''

import math
import time

def combination(n,k): ## <=== INSERT YOUR CODES HERE
    ''' Hint: c(n,k) = n! / (k! * (n-k)! )
    '''
    
    
    return answer

def test():
    n, k = 5, 2 ## <=== test data
    st = time.clock() ## record start time (st)
    answer = combination(n,k)
    print '\ntime elapse: %s' % (time.clock() - st) ## print end time - start time
    print 'c(%s,%s) = %s' % (n, k, answer)

    n, k = 500, 188 ## <=== test data
    st = time.clock()
    answer = combination(n,k)
    print '\ntime elapse: %s' % (time.clock() - st)
    print 'c(%s,%s) = %s' % (n, k, answer)
    
if __name__ == '__main__':
    test()