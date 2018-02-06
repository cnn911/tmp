# -*- coding:utf-8 -*-
"""
created on 2018 1-24
author cnn
"""
'''
原型模式：当一个对象的创建相当繁琐，或者一个对象可以有多个场景的多个值的时候，可以用原型模式对对象进行多个拷贝
'''
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_class(cls, *args, **kwargs):
    return cls(*args, **kwargs)

p1 = Point(1,2)
p2 = copy.copy(p1)
p3 = copy.deepcopy(p1)
p4 = p1.__class__(3,4)
