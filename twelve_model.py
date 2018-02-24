# -*- encoding: utf-8 -*-
"""
Created on Tue Jan 23 21:51:57 2018

@author: Administrator
"""
'''
组合模式：它是结构型模式的一种，他也是利用现有的对象组成一个需要的对象，他与建造模式的区别在于：
组合模式是由一个个可以运行的单独的个体来组成整个对象，而建造者模式主要是由一个个部分组成成一个可以运行的单独个体。
我感觉组合模式中的个体可以由建造者模式来完成，但是反过来就不行。
'''
class Company:
    def __init__(self, name):
        self.name = name

    def add(self, comp):
        pass

    def remove(self, comp):
        pass

    def display(self, dept):
        pass


class Trunk(Company):

    def __init__(self, name):
        Company.__init__(self, name)
        self.child = []

    def add(self, comp):
        self.child.append(comp)

    def remove(self, comp):
        self.child.pop(comp)

    def display(self):
        print(self.name)


class Branch(Company):

    def __init__(self, name):
        Company.__init__(self, name)

    def display(self):
        print('this is end')

def main():
    root = Trunk('first')
    root.add(Branch('cnn'))
    root.add(Branch('wwv'))

    com =Trunk('second')
    com.add(Branch('ss'))
    com.add(Branch('qq'))

    root.add(com)