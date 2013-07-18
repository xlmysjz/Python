#-*-coding:utf-8-*-
'''
Created on 2013-7-18

@author: Administrator

��һ��txt�ļ�����д�����˺ţ�Ȼ�� ��ȡ���txt�ļ���� �˺��ظ���¼

'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time
import HTMLTestRunner

class LoginIn(unittest.TestCase):#
    def setUp(self):
        self.cdr=webdriver.Chrome()
        self.Url="http://www.topka.cn"
    def test_Login(self,username):
        cdr=self.cdr
        Url=self.Url
        cdr.get(Url)
        #cdr.implicitly_wait(5)
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]"))
        
        time.sleep(2)
        cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#�����¼
        
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
        cdr.find_element_by_id("email_login").click()#���ʹ�������½
        print cdr.find_element_by_id("email_login").get_attribute("title")
        
        #�����û�������
        time.sleep(2)
        cdr.find_element_by_id("login_email").send_keys(username)
        print "��¼�û���Ϊ:"+username
        cdr.find_element_by_id("login_password").send_keys("123456")
        cdr.find_element_by_id("remember_me").click()#ȥ����ס��½ checkbox
        #�����¼��ť
        cdr.find_element_by_id("login").click()
        
        time.sleep(5)
        #����ƶ��� ͷ���Աߵ������ͷ��
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
        #�����˵���� �˳��ʺ�
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        
    def test_LoginRead(self):
        cdr=self.cdr
        Url=self.Url
        cdr.get(Url)
        #cdr.implicitly_wait(5)
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]"))
        
        fopen=open(r".\something\username.txt","r")
        for us in fopen:#------�����Ǵ��ļ�����ж�ȡ
            time.sleep(2)
            cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#�����¼
            
            WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
            cdr.find_element_by_id("email_login").click()#���ʹ�������½
            print cdr.find_element_by_id("email_login").get_attribute("title")
            
            #�����û�������
            time.sleep(2)
            cdr.find_element_by_id("login_email").send_keys(us)
            print "��¼�û���Ϊ:"+us
            cdr.find_element_by_id("login_password").send_keys("123456")
            cdr.find_element_by_id("remember_me").click()#ȥ����ס��½ checkbox
            #�����¼��ť
            cdr.find_element_by_id("login").click()
            
            time.sleep(5)
            #����ƶ��� ͷ���Աߵ������ͷ��
            action=ActionChains(cdr)
            action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
            #�����˵���� �˳��ʺ�
            cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        fopen.close()
        
    def tearDown(self):
        #����˳������
        time.sleep(2)
        cdr=self.cdr
        cdr.quit()
        
if __name__=="__main__":
    '''
    #������ �� username.txt ���ȡ���¼
    suite=LoginIn()
    suite.setUp()
    f=open(r".\something\username.txt","r")
    for user in f:
        suite.test_Login(user)
    f.close()
    suite.tearDown()
    '''
    '''
    #���ʹ������ķ��� Ҫ��
    1.class LoginIn(unittest.TestCase)����Ĳ���ȥ����
    2.�� def test_LoginRead(self) ȫ��ע��
    '''

    #������ʹ�� unittest�Լ����ɲ��Ա���----------------
    suite=unittest.TestSuite()
    suite.addTest(LoginIn("test_LoginRead"))
    #���������ɱ���
    filename=".\\something\\LoginReport.html"
    fp=open(filename,"w")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="login",description="���Ǵ�txt��ȡ��ѭ����¼")
    runner.run(suite)
    
    