#-*-coding:utf-8-*-
'''
Created on 2013-8-5

@author: Administrator
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
        
        #����˳������
        time.sleep(2)
        cdr.quit()
    #def outPage(self):
        
