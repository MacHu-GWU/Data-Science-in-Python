##coding=utf8
##By. Sanhe 2014-06-09
##[标题]统计文本的行数
'''
Problem:
    Given a big text file, which is the best way to count how many line in the file.

Conclusion:
    Use buffer. Even the size larger than your memory, this method still working.
'''
import time
''' 方法1 generator method, yield, enumerate'''
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
''' 方法2 built-in loop method in file object '''
def file_len1(fname):
    with open(fname) as f:
        i = 0
        for line in f:
            i = i + 1
            pass
        return i
    
''' 方法3 load data using buffer ''' ## 最佳方法
def block(file, size = 65500):
    while 1:
        nb = file.read(size)
        if not nb: ## nb not None, then, not nb = False
            break
        yield nb
            
def file_len2(fname): ## BEST method
    with open(fname, 'r') as f:
        return sum(line.count('\n') for line in block(f))
    
''' ====================== test ======================= '''
n = 10 ## iterate time
fname = 'data.txt' ## put a text file under same folder
t1,t2,t3,t4,t5 = 0,0,0,0,0
for ii in range(n):
    ''' test1 '''
    st = time.clock()
    data = open(fname)
    i = 0
    for line in data:
        i += 1
        pass
    t1 += time.clock() - st
    print i
    
    ''' test2 '''
    st = time.clock()
    i = file_len(fname)
    t2 += time.clock() - st
    print i
    
    ''' test3 '''
    st = time.clock()
    i = file_len1(fname) ## second Best method
    t3 += time.clock() - st
    print i
    
    ''' test4 '''
    st = time.clock()
    i = sum(1 for line in open(fname))
    t4 += time.clock() - st
    print i
    
    ''' test5 '''
    st = time.clock()
    i = file_len2(fname) ## BEST method !!
    t5 += time.clock() - st
    print i
print t1, '\n', t2, '\n', t3, '\n', t4, '\n', t5, '\n'