#-*-coding:utf-8-*-
'''
Created on 2013-5-7

@author: Administrator
'''
import unittest
def Square(x):
    '''square a number and return the result
    >>>square(2)
    4
    >>>square(3)
    9
    '''
    return x*x
def product(x,y):
    #return x*y #如果是return x*y 则会提示ok
    pass  #如果改成pass就会出现错误的测试
class ProductTestCase(unittest.TestCase):
    def testIntegers(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                p=product(x,y)
                self.failUnless(p==x*y,"Integers failed")
    def testFloats(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                x=x/10.0
                y=y/10.0
                p=product(x,y)
                self.failUnless(p==x*y,"Floats failed")
if __name__=="__main__":
    unittest.main()
            

    