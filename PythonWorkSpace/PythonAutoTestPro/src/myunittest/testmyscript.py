#-*-coding:utf-8-*-
'''
script ��д���ǽű�

��ģ���� ���Խű�,���ҽ����� module ʱ������test��ͷ���� textxx.py

������setUp����ʼ������tearDown������,��Ҫ�õ��ĺ����ǣ�
self.fail([msg])���������ĵ��²���ʧ�ܣ����Ƽ�ʹ�á�
assert "ss" in "asdfsssff" #�ж��Ƿ����
self.assertEqual(value1, value2, failedinfo) # ����value1 == value2
self.assertTrue(����ʽ, failedinfo) # ����valueΪ��
self.assertFalse(����ʽ, failedinfo) # ����valueΪ��
'''
import unittest,script
import HTMLTestRunner
class mytest(unittest.TestCase):
    def setUP(self):
        pass
    def tesrDown(self):
        pass
    
    #�����ǲ�������
    def test_BeginANDend(self):#A����B��ͷ����C��β�������ַ��� ������
        A=["BsC","BafaC","dff"]
        assert "BsC" in script.myscript().foo(A, "B", "C")
        assert "BafaC" in script.myscript().foo(A, "B", "C")
        
    def test_MaxN(self):#��֤ ����A������3����֮�����Ϊ11 
        A = [2, -3, 5, 0, 6, -4]
        num=script.myscript().maxNum(A)
        self.assertEqual(num,11, "���ֵ��11")
        #self.assertEqual(num,12, "���ֵ��11")#�����Ǹ��ǶԵ�
    
def suite():
    
    suite = unittest.TestSuite()
    suite.addTest(mytest("test_BeginANDend"))
    suite.addTest(mytest("test_MaxN"))
    return suite

def test_HTMLTestRunner():#����������������ʾ���Ա����õģ���main���ע��
    alltests=unittest.TestSuite()
    alltests.addTest(mytest("test_BeginANDend"))
    alltests.addTest(mytest("test_MaxN"))
    
    filename="D:\\Program Files\\kuaipan\\PythonWorkSpace\\PythonAutoTestPro\\src\\opentest\\something\\report.html"
    fp=file(filename,'w')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="Result",description="TestReport")
    runner.run(alltests)
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
    
    #�������������һ�����Ա��棬���Խ��������һ��ע�͵���һ��
    #test_HTMLTestRunner()
    
    