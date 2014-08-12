##coding=utf8
'''
在数据库测试，算法测试甚至是为了应付领导或客户时，我们需要大量的
人造数据。本文讨论的就是，如何多快好省的生成大量的人造数据。
 
首先，我们要明确的是，在用于统计分析的数据中，我们通常有两类数据：
1. 在数据分析中不具有价值的，不具备明显分布特性的数据。例如：
    人名，街道，ID号码，电话号码等。我们称这一类数据为 nominal数据
2. 具有一定统计特性的，通常是数值化的数据。例如：
    年龄，身高，体重，金钱等。虽然有些数值不是数字变量，可能是逻辑变量
    但是我们姑且称这一类数据为 numeric 数据
     
生成nominal数据需要一个大量的字典模板。而生成numeric数据需要完备
的概率分布模型。对计算机科学家来说，nominal数据比较容易，numeric
数据比较麻烦。而对于统计科学家来说，正好相反。
 
下面，我们用一个实例来说明，如何在python中，生成大量人造数据吧。
 
Challenge:
生成1000个病人的体检数据。
1.名字
2.生日
3.年龄
4.住址
5.电话
6.身高
7.体重
8.血压
9.心率
10.体脂比
前提假设：
血压通常跟心率相关，体脂比通常被身高体重的比例加上年龄共同影响。
 
Analysis:
首先我们确定一下，每个数据单元是什么类型的数据
1.名字    Nominal
2.生日    Nominal
3.年龄    numeric
4.住址    Nominal
5.电话    Nominal
6.身高    numeric
7.体重    numeric
8.血压    numeric
9.心率    numeric
10.体脂比    numeric

Step1 Nominal data
接下来我们就要上工具了，python faker扩展包。
faker是MIT参照Ruby中的Faker gem开发的python环境下用于生成
Nominal数据的扩展包。在这里，我们用他来生成 名字，生日，住址，电话。

faker扩展包安装：
    pypi distribution:  https://pypi.python.org/pypi/fake-factory/0.4.0
    project website:    https://github.com/joke2k/faker

faker-factory用户文档： http://fake-factory.readthedocs.org/en/master/locales/en_US.html
下面是两个简单的faker库用法
'''
''' fake a name, date, address or SSN '''
import faker
def fake_US():
    fake = faker.Factory.create()
    print fake.name()
    print fake.date()
    print fake.address()
    print fake.ssn()

# fake_US()
''' fake a chinese name, address or phone number '''
import faker
def fake_CN():
    fake = faker.Factory.create('zh-CN')
    print fake.name()
    print fake.address()
    print fake.phone_number()
# fake_CN()
'''
所以很简单的我们可以用下面的脚本生成我们需要的四个Nominal数据
'''
# import faker
# fake = faker.Factory.create()
# for i in range(1000):
#     name, DOB, address, tel = fake.name(), fake.date(), fake.address(), fake.phone_number()
#     print [name, DOB, address, tel]

'''
Step2 Numeric data
计算机伪随机数生成原理解析。
我们知道，任何正态分布都可以通过 Y = (X - u)/ delta的变换变成标准正态分布。
那是不是任何分布都可以通过某种变换，从一个已知分布的X，通过一个函数变换得来呢？
答案是肯定的。

设已知 X 的 CDF函数为：
    P{ X <= x } = F1(x)
目标分布 Y 的CDF 函数为:
    P{ Y <= y } = F2(y)
设存在一个变换  Y = H(X) 使得 上面第二式的Y的CDF分布成立。
所以问题现在转化为 已知 F1, F2 求 H
因为 H(X) = Y

P{ H(X) <= y } = P{ X <= H^-1(y)} = F1( H^-1(y) ) = F2(y) 从而解得 H^-1，从而最终得到H函数。

理论上，这个超函数方程都是有解的，只不过是显式还是隐式罢了。如果有兴趣，可以试着推导：
X ~ u(0,1) === H(X) = Y ===> Y ~ u(0,2)

根据上面的结论，试想一下。我们如果有一个 u(0,1)的均匀分布随机数生成器，那么我们只要通过H变换，就能生成
服从任意分布的随机数。

例如，我们想生成服从正态分布，值域是20-70之间的年龄数据
根据3倍方差和95%置信区间原则。我们可以计算出：
mean = u = 0.5*(20+70) = 45
var = sigma = 0.33*(70-45) = 25/3
再由于
X ~ n(0, 1)
Y ~ n(45, 25/3)
Y = X * sigma + u
'''
import numpy as np
n = 5 ## number of sample
u = 45 ## mean
sigma = 25.0/3 ## variance
data = np.random.randn(1,n)
age = data*sigma + u*np.ones( (1,n) )
print age
# 其他的数据，我们可以照葫芦画瓢依样进行。