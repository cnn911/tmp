# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:40:33 2018

@author: Administrator
"""
'''
状态模式：
当一个对象的状态改变时允许改变其行为，不同的状态就是不同的类
但是却是在同一个方法中实现
当一个对象内在状态改变是允许改变其行为， 这个对象看起来像是改变了类
'''
from state import curr,switch,stateful,State,behavior
from state_machine import before,State

@stateful
class People(object):
    class Workday(State):
        default=True
        @behavior
        def day(self):
            print 'work'
    class weekday(State):
        @behavior
        def day(self):
            print 'week'
people=People()
while True:
    for i in xrange(1,8):
        if i==6:
            switch(people,People.weekday)
        if i==1:
            switch(people,People.Workday)                        
        people.day()



class State:
    def writeprogram(self):
        pass
    
    
class Work:
    def __init__(self):
        self.hour=9
        self.current=Noonstate()
    def SetState(self,temp):
        self.current=temp
    def writeprogram(self):
        self.current.writeprogram(self)
        
class Noonstate(State):
    def writeprogram(self,w):
        print 'noon working'
        if w.hour<13:
            print 'fun'
        else:
            print 'reset'


class otherstate(State):
    def writeprogram(self,w):
        if w.hour<10:
            print 'haha'
        else:
            w.SetState(Noonstate())
            w.writeprogram()


if __name__ == '__main__':
    mywork=Work()
    mywork.hour=9
    mywork.writeprogram()
    mywork.hour=14
    mywork.writeprogram()        
                                
        
        
        
        
        
        
        
        
        
        