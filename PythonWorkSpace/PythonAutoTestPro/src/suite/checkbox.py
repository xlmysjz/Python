#-*-coding:utf-8-*-
'''
Created on 2013-8-5

@author: Administrator
'''
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class selectCheckBox(object):
    def __init__(self):
        global cdr,URL
        cdr=webdriver.Chrome()
        URL="http://www.topka.cn"
        cdr.implicitly_wait(3)
    def test_Info(self):
        cdr.get(URL)
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]"))
        time.sleep(2)
        cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#�����¼
        
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
        cdr.find_element_by_id("email_login").click()#���ʹ�������½
        print cdr.find_element_by_id("email_login").get_attribute("title")
        #�����û�������
        time.sleep(2)
        cdr.find_element_by_id("login_email").send_keys("111111@sina.com")
        cdr.find_element_by_id("login_password").send_keys("123456")
        cdr.find_element_by_id("remember_me").click()#ȥ����ס��½ checkbox
        #�����¼��ť
        cdr.find_element_by_id("login").click()
        
        time.sleep(5)
        #����ƶ��� ͷ���Աߵ������ͷ��
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()

        #�����˵���� ��������
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[3]/a").click()
        #���ר�Ҵ�����֤ ��ǩ
        time.sleep(3)
        cdr.find_element_by_xpath("//div[@class='shelfsetul']/ul/li[6]/a").click()
        
        #ȫ��ѡ�� topka-��������-ר�Ҵ�����֤-�ó�������� checkbox
        #cdr.find_element_by_xpath("//li[@id='goodat_area']/input[1]").click()
        
        #ʹ�üӸ����� find_elements_by_xpath ȫ�����һ�� checkbox,����һ���������ŷ���
        for cli in cdr.find_elements_by_xpath("//input[contains(@type,'checkbox')]"):#���Ҳ��"//input[@type='checkbox']"
            cli.click()
        
        time.sleep(2)
        #����ƶ��� ͷ���Աߵ������ͷ��
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
        #�����˵���� �˳��ʺ�
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        
        cdr.quit()
    #def outpage(self):
        