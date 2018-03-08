# -*- encoding: utf-8 -*-
"""
Created on Tue Jan 23 21:51:57 2018

@author: Administrator
"""
'''
策略模式：它是一种行为型模式。用接口类来实现算法的大体框架，然后根据不同的需求来实现具体的细节。。
他主要是针对行为，活动，算法这类动态内容，所以被称之为行为型模式？
他不同与工厂模式的地方可能在于他针对的是类行为型的对象。

有的时候子类里的行为、状态是不断更新，增加的，所以如果从父类继承的话需要不断的增加所以并不合适，这时候就需要
把变化的部分抽象出来，然后独自形成一个框架。
完成一个事物我需要的是什么？
'''
from abc import ABC
from abc import abstractmethod
from collections import namedtuple

customer =namedtuple('test', 'name price')
class Line:

    def __init__(self, price):
        self.price = price

    def total(self):
        return self.price


class ZongJia:

    def __init__(self, cart):
        self.cart = cart

    def total(self):
        self._total = sum( i.total() for i in self.cart)
        return self._total


class Prom(ABC):

    @abstractmethod
    def dicount(self, zongjia):
        pass


class FirstCount(Prom):

    def discount(self, zongjia):
        return 0.7*zongjia


class SecondCount(Prom):

    def dicount(self, zongjia):
        return zongjia-20



