'''
Created on 2013-5-24

@author: Administrator
'''
import urllib
import urllib2
import cookielib
import json
import re

class Login_kp:
    def __init__(self):
        cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(self.opener)
        self.opener.addheaders = [('User-agent', 'IE')]
    
    def login(self, username, password):
        url = 'https://www.kuaipan.cn/index.php?ac=account&op=login'
        data = urllib.urlencode({'username':username, 'userpwd':password})
        req = urllib2.Request(url, data)
        try:
            fd = self.opener.open(req)
        except Exception, e:
            print(u'�������Ӵ���')
            return False
        if fd.url != "http://www.kuaipan.cn/index.php?ac=fileview":
            print(u"�û��������벻ƥ�䣡")
            return False
        print(u'%s ��½�ɹ���׼��ǩ��..   ' % username),
        return True

    def logout(self):
        url = 'http://www.kuaipan.cn/index.php?ac=account&op=logout'
        req = urllib2.Request(url)
        fd = self.opener.open(req)
        fd.close()
        
    def sign(self):
        url = 'http://www.kuaipan.cn/index.php?ac=common&op=usersign'
        req = urllib2.Request(url)
        fd = self.opener.open(req)
        sign_js = json.loads(fd.read())
        if sign_js['state'] == -102:
            print(u"������ǩ����!")
        elif sign_js['state'] == 1:
            print(u"ǩ���ɹ�! ��û��֣�%d���ܻ��֣�%d����ÿռ䣺%dM\n" % (sign_js['increase'], sign_js['status']['points'], sign_js['rewardsize']))
        else:
            print(u"ǩ��ʧ�ܣ�")
        fd.close()

if __name__ == '__main__':
    l = Login_kp()
    if l.login('your email', 'your password') == False:
        exit(1)
    l.sign()
'''
������ſ�ʼ�˽�python  �õ�����ű���û�����гɹ� ���Ǹ�����ȥ ���շ���ֻҪ��������3�иĳɸ��Ե��˺ž����ˣ�������Ҫע��ĵط����������������﷨����

�����Ǹ��˽�����py�ű����Ϊexe�������̣�

1������py2exe  ����Ǹ�װ��python��Ӧ�汾

2��������ļ��뱻����ļ�����ͬһ���ļ����¡�����

���磬����Ҫ��test.py�����exe����ôtest.py���Ǳ�����ļ�����ô����ļ��أ������±ߵ��ļ�Ϊ.py�ļ� (����setup.py)��

# setup.py

from distutils.core import setup

import py2exe

setup(console=["qiandao.py"])

˵�������һ���������Ϊ��
3��dos�������л��� �����Ľű�Ŀ¼ �������python setup.py py2exe

˵����ǰ�����ѽ�python��װĿ¼�����˻��������������޷��ڴ�����python����

���к󣬵�ǰĿ¼�»����һ��dist�ļ��У�������һ��qiandao.exe�ļ������Ǵ����Ŀ�ִ���ļ���



'''
