##coding=utf8
##By. Sanhe 2014-06-09
##[标题]生成测试数据文本
fname = 'data.txt'
n = 1000000 ## 行数, 1000000行大约70M
with open(fname, 'a') as f:
    for i in range(n):
        f.write(','.join([str(i)] * 10   ) + '\n'  )