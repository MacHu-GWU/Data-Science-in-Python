##coding=utf8
##author=Sanhe
##date=07-13-2014

'''
learn to generate random numbers
    normal distribution
    uniform distribution
    random integer
    random choice
    shuffle
    permutation
'''

import numpy as np ## use np instead of numpy for short

def example1():
    ''' generate random number 
    '''
    print '\nstandard normal distribution:\n%s' % np.random.randn(3,3) ## N(0,1) distribution
    print '\nuniform distribution:\n%s' % np.random.rand(3,3) ## U(0,1) distribution
    print '\nrandom integer array:\n%s' % np.random.randint(1, 5, size = 100) ## in range(#low, #high) generate #size samples
    print '\nrandom choice obey certain distribution:\n%s' %  \
            np.random.choice(a = [11,12,13,14,15], ## a = the sample space
                             size = 3, ## choose how many
                             p=[0.1, 0, 0.3, 0.6, 0]) ## obey what distribution

# example1()

def example2():
    ''' shuffle and permutation
    '''
    array = np.arange(10)
    np.random.shuffle(array) ## np.random.shuffle gonna change the array it self
    print '\nrandomly shuffled:\n%s' % array
    print '\nrandomly arrange:\n%s' % np.random.permutation(10) ## = randperm(10) in matlab

# example2()
