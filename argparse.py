# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:56:16 2017

@author: Administrator
"""

#import argparse
#a=argparse.ArgumentParser(des='This is a sample about argparse')
#a.add_argument('-a',action='store_true',default=False)
#a.add_argument('-b',action='store',default='b')
#
#print a.parse_args(['-a','bva'])
# use the traceback
import sys
import traceback
import inspect
import logging
glist=[1,2,3,4,5]
logging.basicConfig(level=logging.DEBUG,filename='test.txt',filemode='w',\
                    format='%(asctime)s %(filename)s %(lineno)d %(message)s') #设置日志
myname = logging.getLogger(__name__)
def f():
    try:
        print glist[8]
    except Exception,e:
        print e.message
        tr,tv,td= sys.exc_info() 
        traceback.print_exc() #平常的错误信息就是用这个打印的
        logging.critical('error:{0},information{1}'.format(tr,td))
        myname.critical('error is {0}'.format(tv))
        print inspect.trace()


#######多线程
import threading
import time

class test(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay
    def run(self):
        time.sleep(self.delay)
        c=0
        while True:
            c=c+1
            if c==3:
                break
#这是一个基本的多线程阻塞模式
#同事也可以用守护线程
def myfun(a,delay):
    time.sleep(delay)
    result=a*a
    return result



if __name__=='__main__':
    f()
    t1=test('name1',3)
    t2=test('name2',3)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3=threading.Thread(target=myfun,args=(2,5))
    t4=threading.Thread(target=myfun,args=(4,8))
    t3.setDaemon(True)#默认是非守护
    t3.start()
    t4.start()