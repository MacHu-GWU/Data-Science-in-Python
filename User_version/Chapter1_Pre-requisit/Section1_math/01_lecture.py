##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
learn to do power, log, factorial and permulation in python.
Please uncomment the function "example1(), example2(), ..."
one by one to learn the lecture.
'''

import math
def example1():
    '''2 method to do "x to the power y'''
    print '3^4 = %s' % pow(3,4)
    print '2^3 = %s' % 2**3
    ''' exponential function '''
    print 'e^3 = %s' % math.exp(3)
    
# example1()

def example2():
    print 'log e(e) = %s' % math.log(2.718) ## log e(2.718) = 1
    print 'log 10(100) = %s' % ( math.log(100)/math.log(10) ) ## logx(y) = log e(y)/log e(x)
    
# example2()

def example3():
    ''' factorial and permutation '''
    print '5*4*3*2*1 = %s' % math.factorial(5) ## = 5*4*3*2*1, factorial
    print 'P(5,3) = %s' % math.factorial(5)/math.factorial(3) ## = P(5,3), permutation
    
# example3()

def example4():
    ''' other commonly used math function '''
    print 'ceil(5.3) = %s, floor(5.8) = %s' % (math.ceil(5.3), math.floor(5.8))
    flag = raw_input('Enter 1 to see help info... ')
    if flag == '1':
        print help(math) ## print available method

# example4()