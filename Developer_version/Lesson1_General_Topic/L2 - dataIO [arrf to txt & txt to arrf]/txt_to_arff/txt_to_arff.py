##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 把txt中的数据，根据表头的设定，存入一个arrf文件
import os ## py标准库: operation system 操作系统
import arff ## 下载: https://pypi.python.org/pypi/liac-arff

fname = 'segment-challenge.txt'
attrsfname = 'segment-challenge-attributes.txt'
decimator = ','

''' Step1. Check if it is a valid txt file'''
name, ext = os.path.splitext(fname)
if ext != '.txt':
    print 'It is not a *.txt file!'

''' Step2. Load all data in a matrix list(list...) ''' 
data = list()
analysis = list()
with open(fname, 'r') as f:
    for line in f:
        row = line.strip().split(decimator)
        data.append(line.strip().split(decimator))
        analysis.append(len(row))
        if len(set(analysis)) != 1:
            print 'attributes number are not same'
 
n = len(data) ## n: number of sample
m = len(data[0]) ## m: number of attributes include class

''' Step3. Extract attributes infomation '''
attrsinfo = list()
default = 'NUMERIC' ## @@@ Numeric type by default, you can change
with open(attrsfname, 'r') as f:
    for line in f:
        row = line.strip().split()
        if len(row) == 1:
            row.append(default)
            attrsinfo.append(row)
        elif len(row) == 2:
            attrsinfo.append(row)
        else:
            print 'SHIT!'
    for info in attrsinfo:
        info[1] = info[1].upper()

''' Step4. Genterate 'attributes' : VALUE <=== '''
''' Example
1. Nonimal Type Attributes:
    [(u'buying', [u'vhigh', u'high', u'med', u'low']), (u'maint', [u'vhigh', u'high', u'med', u'low'])]
2. Numerica Type Attributes:
    [(u'region-centroid-col', u'NUMERIC'), (u'region-centroid-row', u'NUMERIC')]
'''
dump_to_attributes = list()
for i in range(m):
    attributes = list()
    for row in data:
        attributes.append(row[i])
    if attrsinfo[i][1] == 'NOMINAL':
        dump_to_attributes.append( (attrsinfo[i][0], list(set(attributes)) ) )
    if attrsinfo[i][1] == 'NUMERIC':
        dump_to_attributes.append( (attrsinfo[i][0], 'NUMERIC' ) )

''' Step5. Dump data to arff '''
arffdata = {'description':'', 'relation':'segment', 'attributes':dump_to_attributes, 'data':data}
with open(name+'.arff', 'wb') as f:
    f.write(arff.dumps(arffdata))
            
print 'Complete'