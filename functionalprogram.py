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
#闭包
def count():
	fs = []
	for i in range(1 ,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3 = count()

def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            return lambda : i*i
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

#python中匿名函数
p1=list(filter(lambda s : s and len(s.strip()) > 0 , ['test', None, '', 'str', '  ', 'END']))
print(p1)

#装饰器
def performance(f):
    def print_time(*args, **kw):
        print('call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time())))
        return f(*args,**kw)
    return print_time

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))

#python中带参数decorator
import time

def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            time.sleep(1)
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1)*1000-1000 if unit =='ms' else (t2 - t1)
            print('call %s() in %f %s'%(f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')  
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))
#偏函数 可改变默认的函数参数
import functools

sorted_ignore_case = functools.partial(sorted,key=str.lower)

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))
