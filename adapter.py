# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:05:19 2017

@author: Administrator
"""
'''
this is structure model
then first model is adapter 
this adapter how to achieve?
we can mapping the method to 'execute' keys,then wo can always execute 'execute()'
'''
class Computer:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute(self):
        return 'execute'
        
        
class Human:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return 'say hello'
        
        
class adapter:
    def __init__(self, obj, mapmethod):
        self.objects = obj
        self.__dict__.update(mapmethod)
    def __repr__(self):
        return self.objects
    __str__ = __repr__
   
def main():
    objects=[Computer('caca'),]
    hm = Human('nini')
    objects.append(adapter(hm, dict(execute=hm.speak)))
    for i in objects:
        print i.execute()
if __name__=='__main__':
    main()
    

    