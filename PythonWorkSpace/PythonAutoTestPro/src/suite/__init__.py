#-*-coding:utf-8-*-
'''
���ģ�������ִ��
���ǰ��������� checkbox topkalogin ����ģ��������������ӵ��������ִ��
����������
'''
import unittest,time
from suite import checkbox
from suite import topkalogin
import HTMLTestRunner
from selenium import webdriver

class topkaTestLogin(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_topkaLog(self):#���ǵ�¼topka������
        
        #topkalogin.LoginIn().__init__()#���û�ã����õ���__init__()
        topkalogin.LoginIn().test_LoginRead()#ע��LoginIn���������ƺ�������()��
    
    def test_check(self):#����checkbox������
        
        time.sleep(3)
        #checkbox.selectCheckBox().__init__()#���û�ã����õ���__init__()
        checkbox.selectCheckBox().test_Info()
        
    def tearDown(self):
        pass

def testHtmlTestRunner():
    
    alltest=unittest.TestSuite()
    alltest.addTest(topkaTestLogin("test_topkaLog"))
    alltest.addTest(topkaTestLogin("test_check"))
    
    '''#ע�����������������Ĵ����ǵȼ۵�
    #������ڲ��Ե��������еĲ��Է�������test���� ������makeSuite()����������һ��TestSuite,����ִ��˳���޷���֤
    alltest=unittest.makeSuite(topkaTestLogin,"test")
    '''
    filename=r".\something\Alltestreport.html"
    fp=file(filename,'w')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="AlltestCase",description="TestReport")
    runner.run(alltest)
    
    '''#������Լ��ض��class
    suit1=unittest.TestLoader().loadTestsFromTestCase(topkaTestLogin)
    #suit2=unittest.TestLoader().loadTestsFromTestCase(check)
    alltest=unittest.TestSuite(suit1)
    
    filename=r".\something\Alltestreport.html"
    fp=file(filename,'w')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="AlltestCase",description="TestReport")
    runner.run(alltest)
    '''
    
#ִ������ 
if __name__=="__main__":
    testHtmlTestRunner()

'''#���ַ���Ҳ����ֱ��ִ��
def suite():
    suite = unittest.TestSuite()
    suite.addTest(topkaTest("test_topkaLog"))
    suite.addTest(topkaTest("test_check"))
    return suite
unittest.TextTestRunner().run(suite())
'''
