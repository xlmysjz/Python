#-*-coding:utf-8-*-
'''
����ֻ����֤ ʱ������� �趨ʱ�䣬��ʹ�� js�����ʱ�䣬Ȼ��ű����˳��ˣ�û����������

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import unittest
from datetime import *
import time
import HTMLTestRunner
class createActivity(unittest.TestCase):
    def setUp(self):
        self.cdr=webdriver.Chrome()
        self.cdr.implicitly_wait(3)
        self.URL="http://www.topka.cn"
    def test_ActivityPage(self):
        cdr=self.cdr
        cdr.get(self.URL)
        
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
        
        time.sleep(3)
        #ֱ����ת�� �����ҳ��
        cdr.get("http://topka.cn/activities/create?type=2&cid=1355")
        time.sleep(3)
        
        #�õ�Ԫ���м������<h2>����ۻ�</h2>
        print cdr.find_element_by_xpath("//div[@class='eve_mainbox02']/h2").text
        #�õ�Ԫ�ص�value <input type="text" id="activityName" class="wt490" value maxlength=50>
        print cdr.find_element_by_id("activityName").get_attribute("class")

        cdr.find_element_by_id("activityName").send_keys(unicode("����ʹ�ýű�����Ļ����"))
        
        #�������ص㣬ʹ�õ���JS����ʱ�䣬�����ǵ�ǰʱ�����7��
        #t=time.strftime('%Y-%m-%d',time.localtime(time.time()+7*24*60*60))#����һ�ַ���
        dt=datetime.now()#��ǰʱ��
        t=dt+timedelta(days=7)#timedelta(days=7) ��ָ���7��
        print t.strftime('%Y-%m-%d')
        
        time.sleep(3)
        #���ʼʱ�����ã�ʱ��Ϊ2013-10-09 22ʱ  55��
        #�����ʱ�����ã�ʱ��Ϊ2013-12-20 06ʱ 10��
        #�������ֹ���ã�ʱ��Ϊ2013-12-19 22ʱ 50��
        js="document.getElementById('startDate').removeAttribute('readonly');"+\
            "document.getElementById('startDate').setAttribute('value','2013-10-09');"+\
            "document.getElementById('startTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('startTimeHours').setAttribute('value','22ʱ');")+\
            "document.getElementById('startTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('startTimeMinutes').setAttribute('value','55��');")+\
            "document.getElementById('endDate').removeAttribute('readonly');"+\
            "document.getElementById('endDate').setAttribute('value','2013-12-20');"+\
            "document.getElementById('endTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('endTimeHours').setAttribute('value','06ʱ');")+\
            "document.getElementById('endTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('endTimeMinutes').setAttribute('value','10��');")+\
            "document.getElementById('closeDate').removeAttribute('readonly');"+\
            "document.getElementById('closeDate').setAttribute('value','2013-12-19');"+\
            "document.getElementById('closeTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('closeTimeHours').setAttribute('value','22ʱ');")+\
            "document.getElementById('closeTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('closeTimeMinutes').setAttribute('value','50��');")
             
        #���� unicode ����Ϊ value���к���  ʱ �� ��
        
        cdr.execute_script(js)

        time.sleep(6)
        #����ƶ��� ͷ���Աߵ������ͷ��
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
        #�����˵���� �˳��ʺ�
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        
    def tearDown(self):
        #����˳������
        cdr=self.cdr
        
        cdr.quit()
        
if __name__ =="__main__":
    '''
    suite=createActivity()
    suite.setUp()
    suite.test_ActivityPage()
    suite.tearDown()
    '''
    
    #������ unittest�Լ����ɲ��Ա���
    suite=unittest.TestSuite()
    suite.addTest(createActivity("test_ActivityPage"))
    #unittest.TextTestRunner().run(suite)#�����Ҫ���棬�������ֱ��ִ��
    #���������ɱ���
    filename=".\\something\\createActivityReport.html"
    fp=open(filename,"w")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="createActivityReport",description="This is test_Activity")
    runner.run(suite)
    
    