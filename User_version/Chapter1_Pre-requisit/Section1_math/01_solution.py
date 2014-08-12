##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
Let's take a look at how long your codes takes.
Please copy your codes to the function "combination(n,k)", and run.
Usually the solution is 4-10 times faster than naive implementation.

WHY?
    Time complexity
        c(n,k) = n! / (k! * (n-k)! )
                    n + k + n-k = 2n times multiply
        
               = [ n * (n-1) * ... * (n-k+1) ] / k!
                    k + k = 2k times multiply
    Memory complexity
        for i in xrange(n) is better than for i in range(n)
        Because, range(5) is to generate a "n" length list in
        memory and then cumulatively do the multiply
        But, xrange(n) is to generate only one number each time
        and then do the mutiply. So when n is large, you save
        a lot of memory.
'''

import time
import math
def combination(n,k,answer = -999):
    ''' Copy your codes down here
    '''
    return answer

def combination1(n, k):
    """ A fast way to calculate combination.
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1): ## high performance generator
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def test():
    n, k = 500, 188 ## <=== test data
    st = time.clock()
    answer = combination(n,k)
    print '\nyour codes time elapse: %s' % (time.clock() - st)
    print 'c(%s,%s) = %s' % (n, k, answer)
    st = time.clock()
    answer1 = combination1(n,k)
    print '\nsolution time elapse: %s' % (time.clock() - st)
    print 'c(%s,%s) = %s' % (n, k, answer1)
    
    if answer != answer1:
        print ('\nMaybe you forget to paste your own codes to "def combination(n,k,answer=0):"'
               '\n or your code has something wrong.')
if __name__ == '__main__':
    test()