##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 把arrf中的数据存入txt文件
import os ## py标准库: operation system 操作系统
import arff ## 下载: https://pypi.python.org/pypi/liac-arff

''' ================= HOW TO USE ================== '''
def arff_to_txt(fname, seperator = ','):
    name, ext = os.path.splitext(fname)
    if ext != '.arff': ## 如果扩展名不是.arrf，则抛出异常
        print 'It is not a *.arff file!'
        return
    data = arff.load(open(fname, 'rb'))['data'] ## 从arrf文件中读取存数据
    with open(name + '.txt', 'wb') as f:
        for row in data:
            stringrow = list()
            for i in row: ## convert everything to strings
                stringrow.append(str(i))
            f.write(seperator.join(stringrow) + '\n')
    print 'arff to txt complete!'
    return None

''' arff to txt '''
fname = 'segment-challenge.arff'
arff_to_txt(fname)