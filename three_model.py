# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:30:47 2018

@author: Administrator
"""
'''
发布、订阅模式
发布就是更新数据库后，把数据发送给中心后 能够触发相应的视图进行改变，
订阅就是在关注这个视图后，他的内容能够跟随发布的更新而更新。
这个就像微信：订阅一个主题后，当有消息进行更新时会主动触发发送给订阅者
所以订阅就相当于绑定一系列的事件，在一个主题上发布不同的内容可以触发不同的事件

发布者是数据库，订阅者是视图
pub 发布
sub 订阅
'''

from collections import defaultdict
import message
from message import observable


@observable
class Foo(object):
    def __init__(self,name):
        self.name=name
        self.sub('greet',greeting)
    def pub_greet(self):
        self.pub('greet',self)

route_table = defaultdict(list)
class model(object):
    def sub(self,topic,func):
        if topic in route_table.keys():
            return
        route_table[topic].append(func)
    def pub(self,topic,*args,**kw):
        for func in route_table[topic]:
            func(*args,**kw)

def greeting(*args,**kw):
    print 'hello',args
    
def bar():
    #这里用来触发相当于print
    message.message.pub('work','q')

def handle_the_work(text):
    print text
    
if __name__ == '__main__':
    message.message.sub('work',handle_the_work)
    bar()
    print 'end'
#    test=model()
#    test.sub('test',greeting)
#    test.pub('test','cnn')
         
        
