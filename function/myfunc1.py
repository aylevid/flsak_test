# coding=utf-8
#函数的定义
#格式

'''
def 函数名()
    函数内容;函数内容;
    函数内容;函数内容;
'''
#实例
def function1(i,j):
    '''这是文档字符串
    为了解释函数的使用说明'''
    k=i+j
    #print a
    return (i,j,k)
u=function1(7,8)
x,y,z=function1(7,8)
print u,x,y,z
print function1.__doc__
help(function1)
