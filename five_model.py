# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:46:03 2018

@author: Administrator
"""

'''
工厂方法(抽象工厂)：
工厂就是生产的地方，根据不同的参数返回不同的类
工厂方法不一定是函数，也可以是一个类，一个。。。
'''
import xml.etree.cElementTree as etree
import json

class Jsonconnector:
    def __init__(self,filepath):
        self.data=dict()
        with open(filepath,'r',encoding='utf-8') as f:
            self.data=json.load(f)
    @property
    def parse_data(self):
        return self.data

class Xmlconnector:
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)
    @property
    def parse_data(self):
        return self.tree


def create_factory(filepath):
    if filepath.endswith('json'):
        connector=Jsonconnector
    else:
        connector = Xmlconnector
    return connector(filepath)
def main():
    json_factory = create_factory('test.json')
    data1 = json_factory.parse_data
    print data1


class Operat_add:
    def __init__(self, opa, opb):
        self.opa = opa
        self.opb = opb
    def opt(self):
        return self.opa+self.opb
class Operat_sub:
    def __init__(self, opa, opb):
        self.opa = opa
        self.opb = opb
    def opt(self):
        return self.opa+self.opb
class Operat_factory:
    def __init__(self, opa, opb):
        self.tmp=dict()
        self.tmp['+'] = Operat_add(opa, opb)
        self.tmp['-'] = Operat_sub(opa, opb)
    def create_opt(self, oprator):
        return self.tmp[oprator]
def main3():
    opt = raw_input('your operator:')
    opa = int(input('input your first:'))
    opb = int(input('input your second:'))
    algorithm = Operat_factory(opa, opb)
    ch = algorithm.create_opt(opt)
    result = ch.opt()
    print result    
    
        
    

'''
抽象工厂：按照书面意思解释就是一组工厂模式的集合
也就是说有多个工厂方法统一在一个地方进行管理根据不同的条件产生不同的实例
'''
class Frog(object):
    def __init__(self, name):
        self.name = name
    def can_do(self,obstacle):
        print ('we can jump,eat and {}'.format(obstacle.for_what()))

class Obstacle(object):
    def __str__(self):
        return 'a warm'
    def for_what(self):
        return 'stop the hero'
#创建人物
class Warm_world:
    def __init__(self, name):
        self.player=name
    def create_one(self):
        return Frog(self.player)
    def create_other(self):
        return Obstacle()
        
class Soldier:
    def __init__(self, name):
        self.name = name
    def can_do(self):
        print 'we can fire'
class Monster:
    def __str__(self):
        return 'a monster'
    def for_what(self):
        print 'fire the hreo'

#游戏的创建   
class Man_world:
    def __init__(self, name):
        self.player=name
    def create_one(self):
        return Soldier(self.player)
    def create_other(self):
        return Monster()    
                
#开始游戏，即进行交互            
class Start_game:
    def __init__(self, factory):
        self.a = factory.create_one()
        self.b = factory.create_other()
    def play(self):
        self.a.can_do()
    
#用来统一
def main2():
    name = input('input your name:')
    age = input('input your age:')
    game=Warm_world if age < 13 else  Man_world
    a = Start_game(game(name)) 
    a.play()

if __name__ == '__main__':
    main3()
    
    












        