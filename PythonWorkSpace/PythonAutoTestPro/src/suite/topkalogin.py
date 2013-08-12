#-*-coding:utf-8-*-
'''
这是循环登录 topka 的例子
并有如果出错 则截图的功能
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginIn(object):
    def __init__(self):
        global cdr,URL
        cdr=webdriver.Chrome()
        URL="http://www.topka.cn"
        cdr.implicitly_wait(3)
       
    def test_LoginRead(self):
        cdr.get(URL)
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
            try:
                cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
            except:
                cdr.save_screenshot(".//something//err.png")#如果没找到上面的 元素 则截图
        fopen.close()
        
        #最后退出浏览器
        time.sleep(2)
        cdr.quit()
    #def outPage(self):
        

