#-*-encoding:utf-8-*-
'''
#列表（list）:可修改
s1=['abv','s','d']
s1[2]='z'
print s1

#元组（tuple）:不可修改. tuple也是一种list
s2=(1,2,3)
print s2


#集合(set)
a=set('"as""df""ghdd"')
a1='asdfghdd'
b=set('zxdfvb')
print a
print b
print a&b
print a|b
print a-b
print set(a)
print set(a1)    #去除重复元素


#字典（dict）：关联数组
d={1:'Zhang',2:'Li'}
d['three']='Wang'      #添加字典项目
print d


#关于list和sorted函数用法：


classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adam')                 #list是一个可变的有序表，可以往list中追加元素到末尾
print classmates
print classmates[-1]                      #可以用-1做索引，直接获取最后一个元素
classmates.insert(1, 'Jack')               #把元素插入到指定的位置，比如索引号为1的位置
print classmates
classmates.pop(1)                         #要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print classmates

def reversed_cmp(x, y):                 #反序排序(通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序)
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

def reversed_cmp(x, y):                 #反序排序(通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序)
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print reversed_cmp(5,8)

s=sorted(classmates, reversed_cmp)         #排序sorted()函数是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序
s1=sorted(classmates)
print s
print s1

#列表过滤介绍
print [elem for elem in s if elem != "Bob"]         # 过滤掉特殊值Bob，每次Bob出来过滤表达式都不成立
print [elem for elem in s if s.count(elem) == 1]     #过滤出出现一次的元素



#高级特性：

#切片
l=range(2,100,10)          #创建2-99的数列
print l
print l[:6]           #从下标0开始
print l[-5:-1]         #-1表示最后一个元素
print l[-1]
print l[:10:2]         #前10个数，每两个取一个
print l[::9]          #每10个数取一个

'''
#迭代
d = {'a': 1, 'b': 2, 'c': 3}
print d
for v in d.itervalues():               #迭代value
    print v

from collections import Iterable       #通过collections模块的Iterable类型判断一个对象是否可迭代
print isinstance('abc', Iterable)      # str是否可迭代
print isinstance([1,2,3], Iterable)    # list是否可迭代
print isinstance(123, Iterable)        # 整数是否可迭代


for i, value in enumerate(['A', 'B', 'C']):
   print i, value


























