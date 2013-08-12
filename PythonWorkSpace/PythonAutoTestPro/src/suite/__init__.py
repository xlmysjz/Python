#-*-coding:utf-8-*-
'''
多个模块的用例执行
这是把这个包里的 checkbox topkalogin 两个模块里的用例都添加到这里进行执行
并生产报告
'''
import unittest,time
from suite import checkbox
from suite import topkalogin
import HTMLTestRunner
from selenium import webdriver

class topkaTestLogin(unittest.TestCase):
    
    def setUp(self):
        #self.verificationErrors = []

        pass
    
    def test_topkaLog(self):#这是登录topka的用例
        
        #topkalogin.LoginIn().__init__()#这个没用，不用调用__init__()
        topkalogin.LoginIn().test_LoginRead()#注意LoginIn这个类的名称后面是有()的
    
    def test_check(self):#这是checkbox的用例
        
        time.sleep(3)
        #checkbox.selectCheckBox().__init__()#这个没用，不用调用__init__()
        checkbox.selectCheckBox().test_Info()
        
    def tearDown(self):
        #self.assertEqual([], self.verificationErrors)
        pass

def testHtmlTestRunner():
    
    alltest=unittest.TestSuite()
    alltest.addTest(topkaTestLogin("test_topkaLog"))
    alltest.addTest(topkaTestLogin("test_check"))
    
    '''#注意下面这语句与上面的代码是等价的
    #如果用于测试的类中所有的测试方法都以test开， 可以用makeSuite()方法来构造一个TestSuite,但是执行顺序无法保证
    alltest=unittest.makeSuite(topkaTestLogin,"test")
    '''
    filename=r".\something\Alltestreport.html"
    fp=file(filename,'w')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="AlltestCase",description="TestReport")
    runner.run(alltest)
    
    '''#这个可以加载多个class
    suit1=unittest.TestLoader().loadTestsFromTestCase(topkaTestLogin)
    #suit2=unittest.TestLoader().loadTestsFromTestCase(check)
    alltest=unittest.TestSuite(suit1)
    
    filename=r".\something\Alltestreport.html"
    fp=file(filename,'w')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="AlltestCase",description="TestReport")
    runner.run(alltest)
    '''
    
#执行用例 
if __name__=="__main__":
    testHtmlTestRunner()

'''#这种方法也可以直接执行
def suite():
    suite = unittest.TestSuite()
    suite.addTest(topkaTest("test_topkaLog"))
    suite.addTest(topkaTest("test_check"))
    return suite
unittest.TextTestRunner().run(suite())
'''

