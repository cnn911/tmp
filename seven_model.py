# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:48:39 2018

@author: Administrator
"""

'''
单实例模式：什么是单实例模式？就是只有一个实例吗？那么多地方要用到，怎么可能只有一个实例呢？
感觉怪怪的。然后突然想到把实例的创建放到一个class获得fun中不就行了？不知道这样对不对。。
这个思想有点偏差了。
中间插入一点协奏曲
方法一：
首先可以通过重写__new__方法来将类的实例绑定到变量上
'''
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date1 = cls(day, month, year)
        return date1
        
    @staticmethod
    def is_date(date_string):
        day, month, year = map(int, date_string.split('-'))
        return day
        
new_year = Date.is_date('2018-10-11')
date2 =Date.from_string('2018-01-23')
#print date2
#print new_year

class Datetime(Date):
    def display(self):
        return '*'*20
        
date3 = Datetime(10,10,2001)
date4 = Datetime.is_date('2018-11-11')
print(isinstance(date4, Datetime))
print(date4)

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            origin = super(Singleton, cls)
            cls._instance = origin.__new__(cls, *args, **kw)
        return cls._instance

        
class Myclass_1(Singleton):
    a=1
    
one = Myclass_1()
two = Myclass_1()        
one.a = 4
print(two.a)

#方法二所有实例拥有相同的属性
class Singleton2:
    #we can load all same method to this dict
    _state = dict()
    def __new__(cls, *args, **kwargs):
        ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ob.__dict__.update(cls._state)
        return ob
class Myclass_2(Singleton2):
    a = 2
three = Myclass_2()
four = Myclass_2()

#方法三 用修饰器
def decorate(cls, *args, **kwargs):
    instance = dict()
    def _sington():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _sington

@decorate
class Myclass_3:
    a=2
    def __init__(self, x=0):
        self.x = x

one = Myclass_3()
two = Myclass_3()
id(one) == id(two)
