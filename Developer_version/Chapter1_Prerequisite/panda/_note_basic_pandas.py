##coding=utf8
##reference: http://pandas.pydata.org/pandas-docs/stable/10min.html
import pandas as pd
import numpy as np

''' === pandas 一维序列 === '''
def demo1_pd_Series():
    '''1. 定义基本序列
    '''
    s = pd.Series([1,3,5,np.nan,6,8])
    print s

# demo1_pd_array()

def demo2_pd_indexed_Series():
    '''2. 定义带index的序列
    '''
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    s = pd.Series(sdata)
    print '\ns:\n%s' % s
    print '\ns.index:\n%s' % s.index
    print '\ns.values:\n%s' % s.values
    
# demo2_pd_indexed_array()

''' === pandas 二维表 === '''
def demo3_pd_DataFrame():
    '''3.pandas基本二维表
    '''
    df = pd.DataFrame(np.random.randn(6,4))
    print '\ndf:\n%s' % df
    df.loc[[1],[2]] = 100
    print '\n', df
    print '\n', df.loc[4:5,:] ## 选择行
    print '\n', df.loc[:, 2:3] ## 选择列
    print '\n', df.loc[1:3, 2:3] ## 根据行和列的index选择数据
    
# demo3_pd_DataFrame()

def demo4_pd_indexed_DataFrame():
    '''4.pandas 带index的二维表
    '''
    dates = pd.date_range('20130101',periods=6)
    cindex = list('ABCD')
    print dates ## 行标号
    print cindex ## 列标号
    df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=cindex)
    print '\ndf:\n%s' % df
    print '\ndf.T:\n%s' % df.T ## 转置
    print '\ndf.head():\n%s' % df.head() ## 去掉最后一行
    print '\ndf.tail():\n%s' % df.tail() ## 去掉第一行
    print '\ndf.index:\n%s' % df.index ## 行标 = 索引
    print '\ndf.columns:\n%s' % df.columns ## 列标 = 列
    print '\ndf.values:\n%s' % df.values ## 值, np对象
    print '\ndf.describe():\n%s' % df.describe() ## 统计每列的基本统计参数
    
    print '\ndf.sort_index(axis=1, ascending=False):\n%s' \
            % df.sort_index(axis=1, ascending=False) ## 按照列标号排序，降序
    print '\ndf.sort(columns="B")\n%s' \
            % df.sort(columns='B', ascending=False) ## 按照B列排序，降序
            
    print '\ndf.where(df > 0)\n%s' \
            % df.where(df > 0)
    print '\ndf.mean()\n%s' \
            % df.mean()
    print '\ndf.var()\n%s' \
            % df.var()

# demo4_pd_indexed_DataFrame()

def demo5_pd_indexed_DataFrame_select():
    '''5.pandas 带index的二维表，根据index选择
    '''
    index = range(4)
    cindex = list('ABCDEF')
    df = pd.DataFrame(np.random.randn(4,6), index = index, columns = cindex)
    print '\ndf:\n%s' % df
    print '\ndf.loc[0,:]\n%s' % df.loc[0,:]
    print '\ndf.loc[:,"A"]\n%s\n' % df.loc[:,'A']
    
    ind = np.where(df.values >= 0)
    print '\nnp.where(df.values >= 0) = \n%s' % str(ind)

# demo5_pd_indexed_DataFrame_select()

def demo6_pd_muti_datatype():
    '''6.pandas 二维表， 每列的数据类型各不相同
    '''
    df = pd.DataFrame({'A' : 1.,
                       'B' : pd.Timestamp('20130102'), ## 时间邮戳
                       'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                       'D' : np.array([3] * 4,dtype='int32'),
                       'E' : 'foo' })
    print df
    print df.dtypes
    
# demo6_pd_muti_datatype()
