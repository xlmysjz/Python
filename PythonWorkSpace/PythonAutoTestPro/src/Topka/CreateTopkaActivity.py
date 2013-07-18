#-*-coding:utf-8-*-
'''
这里只是验证 时间输入框 设定时间，即使用 js来填充时间，然后脚本就退出了，没做其他操作

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
        cdr.find_element_by_xpath(".//*[@id='J_connect']/div[2]/div/div/span/a[2]").click()#点击登录
        
        WebDriverWait(cdr,10).until(lambda cdr:cdr.find_element_by_id("email_login"))
        cdr.find_element_by_id("email_login").click()#点击使用邮箱登陆
        print cdr.find_element_by_id("email_login").get_attribute("title")
        
        #输入用户名密码
        time.sleep(2)
        cdr.find_element_by_id("login_email").send_keys("111111@sina.com")
        cdr.find_element_by_id("login_password").send_keys("123456")
        cdr.find_element_by_id("remember_me").click()#去掉记住登陆 checkbox
        #点击登录按钮
        cdr.find_element_by_id("login").click()
        
        time.sleep(3)
        #直接跳转到 创建活动页面
        cdr.get("http://topka.cn/activities/create?type=2&cid=1355")
        time.sleep(3)
        
        #得到元素中间的字体<h2>发起聚会活动</h2>
        print cdr.find_element_by_xpath("//div[@class='eve_mainbox02']/h2").text
        #得到元素的value <input type="text" id="activityName" class="wt490" value maxlength=50>
        print cdr.find_element_by_id("activityName").get_attribute("class")

        cdr.find_element_by_id("activityName").send_keys(unicode("这是使用脚本输入的活动名称"))
        
        #以下是重点，使用调用JS输入时间，下面是当前时间加了7天
        #t=time.strftime('%Y-%m-%d',time.localtime(time.time()+7*24*60*60))#这是一种方法
        dt=datetime.now()#当前时间
        t=dt+timedelta(days=7)#timedelta(days=7) 是指间隔7天
        print t.strftime('%Y-%m-%d')
        
        time.sleep(3)
        #活动开始时间设置，时间为2013-10-09 22时  55分
        #活动结束时间设置，时间为2013-12-20 06时 10分
        #活动报名截止设置，时间为2013-12-19 22时 50分
        js="document.getElementById('startDate').removeAttribute('readonly');"+\
            "document.getElementById('startDate').setAttribute('value','2013-10-09');"+\
            "document.getElementById('startTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('startTimeHours').setAttribute('value','22时');")+\
            "document.getElementById('startTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('startTimeMinutes').setAttribute('value','55分');")+\
            "document.getElementById('endDate').removeAttribute('readonly');"+\
            "document.getElementById('endDate').setAttribute('value','2013-12-20');"+\
            "document.getElementById('endTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('endTimeHours').setAttribute('value','06时');")+\
            "document.getElementById('endTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('endTimeMinutes').setAttribute('value','10分');")+\
            "document.getElementById('closeDate').removeAttribute('readonly');"+\
            "document.getElementById('closeDate').setAttribute('value','2013-12-19');"+\
            "document.getElementById('closeTimeHours').removeAttribute('readonly');"+\
            unicode("document.getElementById('closeTimeHours').setAttribute('value','22时');")+\
            "document.getElementById('closeTimeMinutes').removeAttribute('readonly');"+\
            unicode("document.getElementById('closeTimeMinutes').setAttribute('value','50分');")
             
        #加上 unicode 是因为 value里有汉字  时 和 分
        
        cdr.execute_script(js)

        time.sleep(6)
        #鼠标移动到 头像旁边的下落箭头上
        action=ActionChains(cdr)
        action.move_to_element(cdr.find_element_by_xpath("//div[@class='tr']/div/span[2]")).perform()
        #下拉菜单点击 退出帐号
        cdr.find_element_by_xpath("//div[@class='tr']/div/span[3]/ul/li[4]/a").click()
        
    def tearDown(self):
        #最后退出浏览器
        cdr=self.cdr
        
        cdr.quit()
        
if __name__ =="__main__":
    '''
    suite=createActivity()
    suite.setUp()
    suite.test_ActivityPage()
    suite.tearDown()
    '''
    
    #下面是 unittest以及生成测试报告
    suite=unittest.TestSuite()
    suite.addTest(createActivity("test_ActivityPage"))
    #unittest.TextTestRunner().run(suite)#如果不要报告，这里可以直接执行
    #下面是生成报告
    filename=".\\something\\createActivityReport.html"
    fp=open(filename,"w")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="createActivityReport",description="This is test_Activity")
    runner.run(suite)
    
    