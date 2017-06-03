# python面对对象编程
# 
# 
# 
# python之定义类并创建实例
class Person():
		pass
xiaoming = Person()
xiaohong = Person()
print(xiaoming)
print(xiaohong)

#python创建实例属性
xiaoming.name = "xiaoming"
xiaoming.gender = "male"
xiaoming.birth = "1990-1-1"
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2
xiaohong.grade = xiaohong.grade + 1
print(xiaohong.grade)
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,key=lambda x:x.name)

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)

#python中初始化实例属性
class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__dict__.update(kw)
        
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print(xiaoming.name)
print(xiaoming.job)

#python中访问限制 __属性
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print(p.name)
try :
    print(p.__score)
except AttributeError:
    print('attributeerror')
#python中创建类属性
class Person(object):
    count=0
    def __init__(self,name):
        self.name=name
        Person.count+=1
        
p1 = Person('Bob')
print(Person.count)

p2 = Person('Alice')
print(Person.count)

p3 = Person('Tim')
print(Person.count)
#python中定义实例方法
class Person(object):

    def __init__(self, name, score):
        self.name= name
        self.__score=score

    def get_grade(self):
         if self.__score>=90:
             return "A-优秀"
         elif self.__score >=60:
             return "B-及格"
         else:
             return "C-不及格"
            

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())
#python中方法也是属性
#python中定义类方法
#在class中定义的全部是实例方法
class Person(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
    
print(Person.how_many())

p1 = Person('Bob')

print(Person.how_many())

#python中的继承
#python中继承一个类
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher,self).__init__(name,gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)
#python中多态
#方法调用将作用在 x 的实际类型上。s 是Student类型，它实际上拥有自己的 whoAmI()方法以及从 Person继承的 whoAmI方法，但调用 s.whoAmI()总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。
import json

class Students(object):
    def __init__(self, strlist):
        self.strlist = strlist
        
    def read(self):
        return(self.strlist)

s = Students('["Tim", "Bob", "Alice"]')

print(json.load(s))

#python多重继承
#会打篮球的老师和会踢球的学生
class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin):
    pass

class FTeacher(FootballMixin):
    pass

s = BStudent()
print(s.skill())

t = FTeacher()
print(t.skill())
#python中获取对象信息
#type()获取变量类型
#dir()获得变量的所有属性
class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        self.__dict__.update(kw)

p = Person('Bob', 'Male', age=18, course='Python')
print(p.age)
print(p.course)
l5 = filter(lambda x: x[0]!='_', dir(p))
print(list(l5))
#python中的__str()__和__repr()__
#__str__用于显示给用户
#__repr__用于显示给开发者
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(student: %s,%s,%d)' %(self.name,self.gender,self.score)
    __repr__ = __str__

s = Student('Bob', 'male', 88)
print(s)
#python中的__len__
class Fib(object):

    def __init__(self, num):
        self.num = num
        self.fibo = [0,1]
        i = 2
        while i < self.num:
            self.fibo.append(self.fibo[i-2] + self.fibo[i-1])
            i = i + 1
    
    def __str__(self):
        return str(self.fibo)
    def __len__(self):
        return len(self.fibo)

f = Fib(10)
print(f)
print(len(f))
#python中的数学运算
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        if self.p < self.q:
            k = self.p
        else:
            k = self.q
        for x in range(k, 0, -1):
            if self.p%x==0 and self.q%x == 0:
                self.p = self.p / x
                self.q = self.q / x
                break
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__
        

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)
#python中的类型转换
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
       return self.p *1.0 / self.q

print(float(Rational(7, 2)))
print(float(Rational(1, 3)))
#@property
##@property是get方法
##@score.setter是set方法,它是前一个装饰的副产品
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.__score >= 80:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

s = Student('Bob', 59)
print(s.grade)

s.score = 60
print(s.grade)

s.score = 99
print(s.grade)

#slot
##_slots_是指一个类允许添加的属性列表
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score')

    def __init__(self,name, gender,score):
        super(Student, self).__init__(name, gender)
        self.score = score


s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)
#call
#一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
class Fib(object):
    def __call__(self,num):
        L = [0,1]
        i = 2
        while i < num:
            L.append(L[i-2]+L[i-1])
            i=i+1     
        return L

f = Fib()
print(f(10))