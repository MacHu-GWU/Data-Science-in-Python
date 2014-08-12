##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
What is numpy:
    NumPy is the fundamental package for scientific computing with Python. It contains among other things:
    
    a powerful N-dimensional array object
    sophisticated (broadcasting) functions
    tools for integrating C/C++ and Fortran code
    useful linear algebra, Fourier transform, and random number capabilities
    
Download:
    https://sourceforge.net/projects/numpy/

Install:
    simple double click install
    
if you can run:
import numpy
which means that numpy has been successfully installed
'''

import numpy as np ## use np instead of numpy for short

def example1():
    ''' Create a matrix '''
    data = np.array([[ 0.9526, -0.246, -0.8856],
                     [ 0.5639, 0.2379, 0.9104]])
    print '\ndata = \n%s' % data
    
# example1()

def example2():
    ''' matrix transpose '''
    data = np.array([[ 0.9526, -0.246, -0.8856],
                     [ 0.5639, 0.2379, 0.9104]])
    print '\nT(data) = \n%s' % data.transpose()
    
# example2()

def example3():
    ''' Get elements, vector, sub-matrix 
    Notes:
        In numpy the data structure is like:
        [[row1],
         [row2],
         ...
         [rown]]
        It is a row oriented matrix. So calling A[0]
        is actually call the first row. Their is no 
        column index you can use to call a column
        
    The index in python start from 0, not 1.
    
    
    '''
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    print '\nfirst row = \n%s' % data[0] ## first row
    print '\nfirst column = \n%s' % data.transpose()[0] ## first column
    print '\nDATA23 = %s' % data[(1,2)] ## second row, third column
    print '\n[DATA11, DATA22, DATA33] = %s' % data[[0,1,2],[0,1,2]] ## = data[(0,0)], data[(1,1)], ...
    
# example3()

def example4():
    ''' generate arithmetic progression '''
    data = np.linspace(1,10,10) ## np.linspace(start, end, num)
    print data

# example4()

def example5():
    ''' create basic matrix '''
    print '\nzero matrix:\n%s' % np.zeros((2,3))
    print '\none matrix:\n%s' % np.ones((2,3))
    print '\ndiagonal matrix:\n%s' % np.eye(2,3)

# example5()

def example6():
    ''' shape, and reshape matrix '''
    data = np.array([[ 0.9526, -0.246, -0.8856],
                     [ 0.5639, 0.2379, 0.9104]])
    print data.shape ## return the shape size tuple
    print data.reshape(3,2) ## reshape the matrix row by row
    print data.flatten() ## flatten a 2-d matrix to 1-d array
    
# example6()

def example7():
    ''' value assignment in matrix '''
    data = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
    data[0] = [100,100,100] ## assign first row
    data[(1,1)] = 1000 ## assign DATA22
    print data
    
# example7()