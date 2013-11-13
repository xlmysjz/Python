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
            print(u'网络连接错误！')
            return False
        if fd.url != "http://www.kuaipan.cn/index.php?ac=fileview":
            print(u"用户名跟密码不匹配！")
            return False
        print(u'%s 登陆成功，准备签到..   ' % username),
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
            print(u"今天已签到了!")
        elif sign_js['state'] == 1:
            print(u"签到成功! 获得积分：%d，总积分：%d；获得空间：%dM\n" % (sign_js['increase'], sign_js['status']['points'], sign_js['rewardsize']))
        else:
            print(u"签到失败！")
        fd.close()

if __name__ == '__main__':
    l = Login_kp()
    if l.login('your email', 'your password') == False:
        exit(1)
    l.sign()
'''
因最近才开始了解python  拿到这个脚本后没有运行成功 于是改来该去 最终发现只要将倒数第3行改成各自的账号就行了，其他还要注意的地方就是缩进，否则报语法错误。

下面是个人将以上py脚本打包为exe操作过程：

1、下载py2exe  最好是跟装的python对应版本

2、将打包文件与被打包文件放在同一个文件夹下。。。

例如，你需要将test.py打包成exe，那么test.py就是被打包文件，那么打包文件呢，保存下边的文件为.py文件 (例如setup.py)：

# setup.py

from distutils.core import setup

import py2exe

setup(console=["qiandao.py"])

说明：最后一行里面各自为定
3、dos窗口下切换到 需打包的脚本目录 运行命令：python setup.py py2exe

说明：前提是已将python安装目录设置了环境变量，否则无法在此运行python命令

运行后，当前目录下会产生一个dist文件夹，其下有一个qiandao.exe文件，就是打包后的可执行文件。



'''
