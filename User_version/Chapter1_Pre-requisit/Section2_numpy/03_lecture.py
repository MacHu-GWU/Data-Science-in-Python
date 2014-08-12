##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
learn
    matrix times matrix
    inverse matrix
    vector times vector, inner product
    diagonal matrix
    euclidean norm
    solve linear equation
    matrix decomposition
'''

import numpy as np
import numpy.linalg as npl ## numpy linear algebra
    
def example1():
    ''' Matrix dot with Matrix '''
    A = np.array([[1,2],
                  [3,4]])
    B = np.array([[2,0],
                  [0,2]])
    print np.dot(A,B)

# example1()

def example2():
    ''' find the inverse matrix '''
    A = np.array([[7,3,9],
                  [4,1,8],
                  [5,6,2]])
    print npl.inv(A) ## inverse matrix

# example2()

def example3():
    ''' matrix devided by another matrix '''
    A = np.array([[1,2],
                  [3,4]])
    B = np.array([[2,0],
                  [0,2]])
    C = np.dot(A,B) ## C = A * B
    print np.dot(C, npl.inv(B) ) ## A = C * B^-1

# example3()

def example4():
    ''' Vector dot with Vector '''
    A, B = np.array([1,2,3]), np.array([-1,0,1])
    print np.vdot(A,B) ## flatten 2 matrix, and calculate the inner dot
    print np.inner(A,B) ## inner dot
    print np.outer(A,B) ## outer dot

# example4()

def example5():
    ''' diagonal elements & diagonal matrix'''
    A = np.array([[7,3,9],
                  [4,1,8],
                  [5,6,2],
                  [8,8,8]])
    print '\nthe diagonal elements in matrix A is:\n%s' % np.diagonal(A) ## diagonal elements
    print '\ngenerate diagonal matrix from a vector\n%s' % np.diag(np.array([1,2,3])) ## diagonal matrix
    
example5()


def example6():
    ''' euclidean norm '''
    A = np.array([3,4])
    B = np.array([[3,4],
                  [1,2]])
    print npl.norm(A) ## 求标准二范数 
    print npl.norm(B, axis = 0) ## 基本上所有对向量的操作符，当操作对象为矩阵时，都可以通过设置
    print npl.norm(B, axis = 1) ## axis = 0 or 1 来决定是对行向量操作或是对列向量操作

example6()
''' 解有解的线性方程 '''
# X = np.array([[3,1],[2,4]])
# y = np.array([8,9])
# print npl.solve(X,y)

''' Matrix Decomposition 矩阵分解 '''
''' 奇异值分解 '''
# A = np.array([[7,3,9],
#               [4,1,8],
#               [5,6,2]])
# U,d,V = npl.svd(A) ## 在python中SVD的结果是： U * diag(d) * V = A
# print U ## 正交阵
# print d ## 对角线元素
# print V ## 正交阵
# D = np.diag(d) ## 生成对角阵
# print np.dot(np.dot(U, D), V) ## 计算 U * diag(d) * V

''' QR 分解  以及 Gram Schmidt 标准正交化'''
# A = np.array([[1,1,6],  ## [注意] numpy.linalg 是对列向量进行标准正交化
#               [1,2,4],
#               [1,3,2]])
# q, r = npl.qr(A)
# print '半正交矩阵q:\n', q
# print '上三角矩阵r:\n', r
# print '验证q的正交性:\n', np.dot(q, q.transpose())