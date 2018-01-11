# -*- coding: utf-8 -*-
"""test

Usage:
    descriptor <val>

Options:
    -h --help     Show this screen.
    --version     Show version.

Example:
    descriptor test here 123
"""
from docopt import docopt
class RevealAccess(object):
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        print self.val
    def __set__(self, obj, val):
        print 'updateing',self.name
        self.val=val
class myclass(object):
    x=RevealAccess(10, 'value')
    y=5
if __name__ == '__main__':
    arguments = docopt(__doc__)
    print arguments
    a = myclass()
    val = arguments['<val>']
    a.x=val
    a.y=val
