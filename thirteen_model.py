# -*- encoding: utf-8 -*-
"""
Created on Tue Jan 23 21:51:57 2018

@author: Administrator
"""
'''
命令模式： 顾名思义这个就是把不同的条件作为命令来调用相应对象的动作。
能够想到的就是把命令分装为对象，把要执行的命令封装一个对象，把要执行动作的集合封装一个对象
执行者也可以是对象，也可是函数
'''
class Command(object):
    def __init__(self):
        pass
    def excute(self):
        pass

class Lightswitch(object):
    def __init__(self):
        self._lighton = BrightCommand(Light())
        self._lightoff = DarkCommand(Light())
    def switch(self, cmd):
        if cmd == 'ON':
            self._lighton.excute()
        else:
            self._lightoff.excute()

class BrightCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self._light = light

    def execute(self):
        self._light.turnon()

class DarkCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self._light = light

    def execute(self):
        self._light.turnoff()

class Light(object):
    def turnon(self):
        print('the light is on')

    def turnoff(self):
        print('the light is off')

def main():
    test = Lightswitch()
    test.switch('ON')
    test.switch('OFF')
