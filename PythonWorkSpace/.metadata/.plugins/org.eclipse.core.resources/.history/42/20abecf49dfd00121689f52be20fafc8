#-*-coding:utf-8-*-
'''
Created on 2013-7-18

@author: Administrator

在一个txt文件夹里写几个账号，然后 读取这个txt文件里的 账号重复登录

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
        cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#点击登录
        
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
        cdr.find_element_by_id("email_login").click()#点击使用邮箱登陆
        print cdr.find_element_by_id("email_login").get_attribute("title")
        
        #输入用户名密码
        time.sleep(2)
        cdr.find_element_by_id("login_email").send_keys(username)
        print "登录用户名为:"+username
        cdr.find_element_by_id("login_password").send_keys("123456")
        cdr.find_element_by_id("remember_me").click()#去掉记住登陆 checkbox
        #点击登录按钮
        cdr.find_element_by_id("login").click()
        
        time.sleep(5)
        #鼠标移动到 头像旁边的下落箭头上
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
        #下拉菜单点击 退出帐号
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        
    def test_LoginRead(self):
        cdr=self.cdr
        Url=self.Url
        cdr.get(Url)
        #cdr.implicitly_wait(5)
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]"))
        
        fopen=open(r".\something\username.txt","r")
        for us in fopen:#------这里是从文件里进行读取
            time.sleep(2)
            cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#点击登录
            
            WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
            cdr.find_element_by_id("email_login").click()#点击使用邮箱登陆
            print cdr.find_element_by_id("email_login").get_attribute("title")
            
            #输入用户名密码
            time.sleep(2)
            cdr.find_element_by_id("login_email").send_keys(us)
            print "登录用户名为:"+us
            cdr.find_element_by_id("login_password").send_keys("123456")
            cdr.find_element_by_id("remember_me").click()#去掉记住登陆 checkbox
            #点击登录按钮
            cdr.find_element_by_id("login").click()
            
            time.sleep(5)
            #鼠标移动到 头像旁边的下落箭头上
            action=ActionChains(cdr)
            action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
            #下拉菜单点击 退出帐号
            cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        fopen.close()
        
    def tearDown(self):
        #最后退出浏览器
        time.sleep(2)
        cdr=self.cdr
        cdr.quit()
        
if __name__=="__main__":
    '''
    #这里是 从 username.txt 里读取后登录
    suite=LoginIn()
    suite.setUp()
    f=open(r".\something\username.txt","r")
    for user in f:
        suite.test_Login(user)
    f.close()
    suite.tearDown()
    '''
    '''
    #如果使用上面的方法 要将
    1.class LoginIn(unittest.TestCase)里面的参数去掉，
    2.将 def test_LoginRead(self) 全部注释
    '''

    #这里是使用 unittest以及生成测试报告----------------
    suite=unittest.TestSuite()
    suite.addTest(LoginIn("test_LoginRead"))
    #下面试生成报告
    filename=".\\something\\LoginReport.html"
    fp=open(filename,"w")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="login",description="这是从txt读取后循环登录")
    runner.run(suite)
    
    