#-*-coding:utf-8-*-
'''
Created on 2013-5-24

@author: Administrator
'''
#!/usr/bin/python



#这是网上传的 有人写的一个 去哪网 的一个例子

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re

class QunarSearch(unittest.TestCase):
    
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.mouse = webdriver.ActionChains(self.dr)
        self.dr.implicitly_wait(3)
        self.base_url = "http://www.qunar.com"
        self.verificationErrors = []
   
    def test_input_search_qunar(self):
        dr = self.dr
        mouse = self.dr
        dr.get(self.base_url + "/")
        dr.maximize_window()
        
        # 选择 国内机票
        domestic = dr.find_element_by_id("chinaLine")
        domestic.click()
        time.sleep(1)
        
        # 选择 城市
        src = dr.find_element_by_name("fromCity")
        dst = dr.find_element_by_xpath("//input[@class='textbox flightinput'][@name='toCity']")
        src.clear()
        src.send_keys(unicode("重庆","utf8"))
        time.sleep(1)
        dst.clear()
        dst.send_keys(unicode("昆明","utf8"))
        time.sleep(1)
        
        # 选择 方式
        type = dr.find_element_by_id("searchTypeRnd")
        type.click()
        time.sleep(1)
        
        # 选择 日期
        #点击弹框选择日期方法
        fdata = dr.find_element_by_css_selector("#mainXI2 > div.sicon")
        fdata.click()
        time.sleep(1)
        dr.find_element_by_xpath("//td[@value='2012-09-18']").click()
        time.sleep(1)
        '''
        tdata = dr.find_element_by_css_selector("#mainXI3 > div.sicon")
        tdata.click()
        time.sleep(1)
        dr.find_element_by_xpath("//td[@value='2012-09-26']").click()
        time.sleep(6)
        #直接发送日期的方法
        fdate = dr.find_element_by_xpath("//div[@id='chinaPanel']//input[@name='fromDate']")
        fdate.clear()
        fdate.send_keys("2012-09-15")
        time.sleep(1)
        '''
        tdate = dr.find_element_by_xpath("//div[@id='chinaPanel']//input[@name='toDate']")
        tdate.clear()
        tdate.send_keys("2012-09-26")
        time.sleep(1)
                     
        # 点击搜索
        button = dr.find_element_by_xpath("//div[@id='chinaPanel']//button[@class='searchButton'][@type='submit']")
        button.submit()
        time.sleep(2)
        
        # 搜索页-选择自选模式
        dr.find_element_by_xpath("//div[@class='selectModel']//a[contains(.,'自选模式')]").click()
        time.sleep(2)
        
        # 选择航班组合
        dr.find_element_by_id("hobj南方航空").click()
        time.sleep(2)
        from_flight = dr.find_element_by_id('hdivOutboundResultTable2')
        from_airs = from_flight.find_elements_by_tag_name('input')
        from_airs[1].click()
        time.sleep(1)
        to_flight = dr.find_element_by_id('hdivReturnResultTable2')
        to_airs = to_flight.find_elements_by_tag_name('input')
        to_airs[1].click()
        time.sleep(1)
        dr.find_element_by_css_selector('button.btnAdd').click()
        time.sleep(4)
        
        # 选择一种组合-点击订票
        airline = dr.find_element_by_id('btnBooking10000')
        if airline:
            airline.click()
            time.sleep(2)
            dr.find_element_by_xpath("//td[@class='c1']//a[@class='btnBook']").click()
            time.sleep(2)
            # 切换到新打开的订单填写页
            titles = dr.window_handles
            if titles[1]:
                dr.switch_to_window(titles[1])
                time.sleep(8)
                if not self.assertEqual("订单填写页",dr.title):
                    # 乘机人信息
                    #name = dr.find_element_by_name("passenger_name")
                    #name = dr.find_element_by_css_selector("#passenger_list > input.passenger_name")
                    name = dr.find_element_by_xpath("//div[@id='passenger_list']//input[@name='passenger_name']")
                    name.clear()
                    name.send_keys(unicode("吉蓝风",'utf8'))
                    number = dr.find_element_by_name("passenger_credential_no")
                    number.clear()
                    number.send_keys("451023198207167074")
                    time.sleep(1)
                    # 联系人信息
                    #name2 = dr.find_element_by_name("contact_name")
                    #name2 = dr.find_element_by_css_selector("#module_contact > input.contact_name")
                    name2 = dr.find_element_by_xpath("//div[@id='module_contact']//input[@name='contact_name']")
                    name2.clear()
                    name2.send_keys(unicode("吉蓝风",'utf8'))
                    phone = dr.find_element_by_name("contact_phone")
                    phone.clear()
                    phone.send_keys("18896697878")
                    email = dr.find_element_by_name("contact_email")
                    email.clear()
                    email.send_keys("mbugatti@163.com")
                    time.sleep(8)
                    # 提交订单
                    dr.find_element_by_id("bt_submit").click()
                    time.sleep(3)
                    
                    # 订单确认页
                    # 选择支付方式
                    #dr.find_element_by_xpath("//div[@class='paymode']//input[@id='tenpayCard-1031']").click()
                    #dr.find_element_by_css_selector("#payForm > input.tenpayCard-1031").click()
                    try:
                        dr.find_element_by_xpath("//div[@id='payMethodPanel']//form[@id='payForm']//div[@class='paymode']//a[@class='logo cmb']//input[@id='tenpayCard-1031']").click()
                    except NoSuchElementException:
                        # 点击-立刻支付
                        dr.find_element_by_id("payBtn").click()
                        time.sleep(3)

    def tearDown(self):
        self.dr.quit()
                
if __name__ == "__main__":
    unittest.main()
    
    
