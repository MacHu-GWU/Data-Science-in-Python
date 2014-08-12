##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 漂亮打印arrf文件中的数据
import arff ## 下载：https://pypi.python.org/pypi/liac-arff
import pprint ## py标准库： 漂亮打印机
fname1 = 'car_eva.arrf'
fname2 = 'segment-challenge.arff'
data = arff.load(open(fname, 'rb'))
pprint.pprint(data)