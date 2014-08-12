##coding=utf8
##By. Sanhe 2014-06-09
# [标题] 在从文本读取数据时，如果定义了每一列不同的数据格式，
# 则numpy.narray中的元素都被读成了不可变的元组。此时就无法
# 使用 np.transpose()等特殊方法。此时如果要对列进行操作的话，
# 就需要使用到读取数据时，对每一列的名称定义。然后可以通过
# np['name']的方式调用、赋值
import numpy as np
from StringIO import StringIO
with open('dump_data3.txt', 'rb') as text:
    data = np.genfromtxt(   StringIO(text.read()), 
                            delimiter=",", ## 定义分隔符
                            dtype = [('x', int), ('y', float), ('z', 'S10')], ## 定义数据类型
                            skiprows = 0, ## 从头跳过若干行
                            skip_header = 0, ## 跳过第一行标题
                            skip_footer = 0) ## 跳过最后一行注脚

print data ## 打印数据
print data['x'], data['y'], data['z'] ## 取得各个列
data['x'] = [100,400,700] ## 对列赋值
print data['x'] ## 检查赋值是否生效了