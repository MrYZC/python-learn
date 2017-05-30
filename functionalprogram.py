# python函数式编程
# 变量可以指向函数
# 函数名指向一个函数对象
# 高阶函数：能够接受函数作为参数的函数
# 1.python把函数作为参数
import math
from functools import reduce

def add(x, y, f):
    return f(x) + f(y)

print(add(25, 9, math.sqrt))
#2.python中的map()函数
def format_name(s):
   return s.capitalize()
r=map(format_name,['adma', 'LISA' ,'barT'])
print(list(r))
#3.python中的reduce()函数
def prod(x, y):
	return x * y
print(reduce(prod,[2,4,5,7,12]))
#4.python中的filter()函数
def is_sqr(x):
	return math.sqrt(x)%1==0
g=filter(is_sqr,range(1,101))
print(list(g))
#python中自定义排序函数
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
#python中的返回函数
def calc_prod(lst):
    def prod():
        return reduce(lambda x, y : x * y, lst)
    return prod

f = calc_prod([1, 2, 3, 4])
print(f())