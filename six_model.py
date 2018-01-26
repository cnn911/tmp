# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:51:57 2018

@author: Administrator
"""

'''
建造者模式：它是属于创建型一类的模式，何为建造者模式，根据书上的理解来说就是
需要一个指挥者来根据需求完成对象的创建不同的需求就是一个不同的类。但是他们一般又是从同一个
抽象类里继承来的。
'''
class Person:
    def handles(self):
        pass
    def head(self):
        pass
    def body(self):
        pass
    def feet(self):
        pass


class ThinPerson(Person):
    def handles(self):
        print 'thin hands'
    def head(self):
        print 'thin head'
    def body(self):
        print 'thin body'
    def feet(self):
        print 'thin feet'


class TailPerson(Person):
    def handles(self):
        print 'tail person'
    def body(self):
        print 'tail person'
    def head(self):
        print 'tail head'
#根据不同的需求创建不同的类
#然后完成指挥者


class Dictor:
    def __init__(self,p):
        self.tmp=p
    def create(self):
        self.tmp.handler()
        self.tmp.body()
    

def main():
    height = input('input height:')
    person = ThinPerson if height<200 else TailPerson
    one = Dictor(person())
    one.create()


    




