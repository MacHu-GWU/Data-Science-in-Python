##coding=utf8
##By. Sanhe 2014-06-09
##[标题]快速并以最小内存读取大文本内的数据
'''
Problem1:
    given a big data, no larger than your memory, how to load it fast

Conclusion:
    Just use this, it is the built-in fastest way
        f = open(fname, 'r')
        for line in f.xreadlines():
            pass
'''
## create any large text your self, just copy and paste
fname = 'data.txt'
import time

''' method 1 '''
f = open(fname,'r')
st = time.clock()
while 1:
    lines = f.readlines(1000000)
    if not lines:
        break
    for line in lines:
        pass # do something
print 'method 1 takes: ',time.clock()-st
f.close()

''' method 2 ''' ## 时间上f.read()和f.xreadlines()差不多
f = open(fname,'r')
st = time.clock()
for line in f:
    pass # do something
print 'method 2 takes: ', time.clock()-st
f.close()

''' method 3 ''' ## 内存上f.read()比f.xreadlines()消耗大的多
f = open(fname, 'r')
st = time.clock()
for line in f.xreadlines():
    pass # do something
print 'method 3 takes: ', time.clock() -st
f.close()