#-*-coding:utf-8-*-
import math
from math import sqrt
import copy
import tt
import time
import random
import re

'''
print math.floor(32.9) 
print int(math.floor(32.9))
print sqrt(9)#��������� from math import sqrt ��Ͳ���math.sqrt(x),��ֱ���� sqrt(x)

print "let's go," "ok"

temp=42
print"this is "+repr(temp)#repr(x)�ǽ�ֵת��Ϊ�ַ�����Ҳ����ʹ��str(x)

name=raw_input("what's you name:")
print "hello "+name+"!"
'''

'''
print "hello\nword"#���з�\n
print r"c:\Program Files\name" #���ʹ�� r ���ַ���������治������ \,����  r"c:\Program Files\name\" �Ǵ����
print "c:\\Program Files\\name\\"
print round(5.34,1)#����һλС��
'''

'''
#ð������1
num=[34,12,8,21,55,-1]
for i in range(len(num)):
    for j in range(len(num)-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
    print num
#ð������2
def maoPao(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                tem=num[j]
                num[j]=num[j+1]
                num[j+1]=tem
    print num
print"-"*20
num=[34,12,8,21,55,-1,10]
maoPao(num)
'''

'''
greet="hello"
print greet[0]
print greet[-4]

inp=raw_input("���������֣������ӡ�����ĸ�ֵ")[3]
print inp
'''

'''#�����Ϊ�� ��ӡ����Ӧ�� �� �� ��
months=["january","february","march","april","may","june","july","august","september","october",
        "november","december"]
endings=["st","nd","rd"]+17*["th"]+["st","nd","rd"]+7*["th"]+["st"]#���ֻ��Ϊ��д����ĺ�׺ ��st nd rd th

year=raw_input("Year:")
month=raw_input("month(1-12):")
day=raw_input("day(1-31):")

month_number=int(month)
day_number=int(day)

#Ҫ���·ݺ�������һ���Ի�ȡ��ȷ������
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]

print month_name+" "+ordinal+", "+year
'''

#��Ƭ
'''
t=[1,2, 3, 4, 5, 6, 7, 8, 9, 10]
print t[3:9]
print t[9:4:-1]#����и�����Ϊ ��������Ϊ�Ӵ�С д ����
print t[5::-1]#����и�����Ϊ ��������Ϊ�Ӵ�С д ����
print t[:5:-1]#����и�����Ϊ ��������Ϊ�Ӵ�С д ����
print t[9:3:-2]#����Ϊ2ʱ
print t[-9:6]#����������� Ԫ�� ���� ���ұߵ� Ԫ�� ���ֵ��� �ſ��Դ�ӡ
'''

#len min max
'''
num=[100,30,66,23,100]
print len(num)
print min(num)
print max(num)

name=["a","b","c","d"]
del name[2] #ɾ���б��е�Ԫ��
print name
'''
'''
#��Ƭ
name=list("perll")#������ת�����б�
print name #��ӡ�������� ['p', 'e', 'r', 'l']
name[2:]= list("ar")
print name

num=[1,5]
num[1:1]=[2,3,4]#���滻�κ�Ԫ�ص�����²����µ�Ԫ��
print num

num=[1,2,3,4,5,6]
num[1:4]=[]#��ֵɾ��
print num
'''
'''
#append()
num=[1,2]
num.append(3) #����append()���������б����Ԫ��
print num

a=[1,2,1,1,2,3,2,3]
print a.count(1)#ͳ��1���ֵĴ���

#extend()
a=[1,2,3]
b=[4,5,6]
a.extend(b) #��a�б���һ������b�б��е�Ԫ��
print a
print b

#insert
num=[1,2,3,4]
num.insert(2, "name")#ֻ�ǲ���һ��Ԫ�أ�����ɾ�������Ԫ��
print num

#pop
a=["a","b","c","d"]
a.pop(1)#�Ƴ��±���1��Ԫ��
print a
print a.pop()#�������д�±� Ĭ���Ƴ����һ��,�����Ƴ����Ǹ�Ԫ�ط���
print a

#remove
num=["to","bo","co","do"]
num.remove("to")#ֱ���Ƴ�ĳ��Ԫ��
print num

#reverse��ת
a=["ao","bo","co"]
a.reverse()#��Ԫ�ط�����
print a
'''
'''
#sort()����
num=[3,1,3,4,43,23,25]
num.sort()#��num�б���������
print num

num=[100,90,30,40,80,20,10]
a=num[:]#��num�б�������a
a.sort()#�ڶ�a���������������Բ��ı�ԭ����num�б���ֵ
print num
print a

number=[5,3,8,9]
number.sort(cmp)
print number

num=[5,2,9,7,10]
num.sort(reverse=True)#reverse=True�ǰ��յ������У� reverse=False�ǰ�����������
print num

#sorted ��ȡ��������б������ķ���
x=[2,1,67,5,4,7]
y=sorted(x)
print x
print y

'''

'''
#2.4Ԫ��
(42,)#���Ԫ����ֻ��һ��ֵ��Ҳ�����ж���

#tuple�ǽ�һ������ת��ΪԪ�飬�����Ԫ�飬��ԭ������
print tuple([1,2,3])
print tuple(("a","b","c"))
x=(1,2,3)
print x[1]
print list(x)
'''
'''
#3.4
#find
title="hellor word"
print title.find("wo")#��������˵��±�
print title.find("a")#û�ҵ�������-1
print "h"in title# in ֻ�� �жϵ����ַ� find���Բ��Ҷ���ַ�
print title.find("ll",1)#�ṩ����ʼ��1��ʼ������
print title.find("or",5,10)#�ṩ�� ��ʼ��5,������10 ����
'''
'''
#join ����������Ԫ��,���ӵĶ���Ԫ�ض��������ַ���
a=[1,2,3,4]
b="+"
b.join(a) #���Ǹ������ ����

a=["a","b","c"]
b="+"
print b.join(a)#��ӡ���ǣ�a+b+c

dir="","usr","bin","env"
print"/".join(dir) #��ӡ���ǣ�/usr/bin/env


#lower ����дת��ΪСд
title="This My name"
print title.lower()

myname="LiLei"
name=["lili","lilei","Tom"]
if myname.lower() in name: #������������Ա��� �����ִ�Сд �ķ���
    print "I found"

#replace �ַ���������ƥ��������滻֮��õ����ַ���
name="this is lilei"
print name.replace("lilei","Tom")

#split���ַ����ָ�Ϊ ����
sentence="this/is/my/name"
print sentence.split("/")
'''
'''
#strip ȥ���ַ������˵� �ո�
sentence="  this  my name  "
print sentence.strip()

myname="lili  "#���ֺ����пո�
name=["lili","lilei","Tom"]
if myname.strip() in name: #ȥ�����ֺ���Ŀո񣬲����Ƿ��� name ������
    print "I found "
    
a="Tthis is ListT"
print a.strip("T")#ֻ��ȥ������� T
'''
'''
#�ֵ�
phonebook={"Alice":"12","lilei":"34","Tom":"56"}
print phonebook["Tom"]

item=[("name","gumby"),("age",30)]
d=dict(item)#dict()�����ֵ�
print d

d=dict(name="gub",age=30)#�������ַ���
print d

dic={"name":"lilei","age":30,"sex":"nv"}
print len(dic)
print dic["name"]#��ӡ�ֵ��� name �� ֵ
dic["sex"]="nan"#��ֵ nan ������ sex����
print dic

del dic["age"]#ɾ����Ϊ age ����
print dic

print "name" in dic #���d���Ƿ��� name �����

x={}
x["ID"]=50 #�� ֵ50 ������ �� ��
print x
'''

'''
print"---------����ĸ�ʽ���ַ�-------------"
template="<html> \
        <head><title>%(title)s</title></head> \
        <body> \
        <h1>%(title)s</h1> \
        <p>%(text)s</p> \
        </body>"
data={"title":"My Home Page","text":"Welcome to my home page"}
print template % data

print"\n----������һ��д��------"
data={"title":"My Home Page","text":"Welcome to my home page"}
print "���title�� %(title)s" %data

data={"title":"My Home Page","text":"Welcome to my home page"}
print data.clear()#����ֵ����������

'''
'''
#deepcopy��ȿ���
d={}
d["names"]=["Alfred","Bertrand"]
print d
c=d.copy()#ǳ����  ǳ���� ֻ���������󣬲��´��������ڲ����Ӷ���
dc=copy.deepcopy(d)#��ȿ���   ��� �����������Ӷ���

d["names"].append("haha")
print d
print c
print dc


#�ֵ��е�get����
data={"title":"My Home Page","text":"Welcome to my home page"}
print data.get("title")#������ʱ ����ӡ�� ��ְ
print data.get("k")#����û��ʱ ����ӡ��None
print data.get("k","hh")#���û�м������Դ�ӡ��������Ϣ

#�ֵ��е�items����
data={"title":"My Home Page","text":"Welcome to my home page"}
print data.items()#�÷������ֵ����б���ʽ���� [('text', 'Welcome to my home page'), ('title', 'My Home Page')]

it=data.iteritems()#�÷�����items()���ƣ��������ص��ǵ���������������б�
print list(it)

d={"x":1,"y":2}
d.pop("y")#�Ƴ��ֵ���ļ�-ֵ
print d

d={"x":1,"y":2,"z":3}
print d.popitem()#����Ƴ� ��-ֵ,�����Ƴ����Ǹ���-ֵ ��ӡ
print d
'''
'''
#�ֵ����setdefault  
data={"title":"My Home Page","text":"Welcome to my home page"}
print data.setdefault("title")# �����������������ֵ

data.setdefault("name","t")#�ڲ����и�������������趨��Ӧ�� ֵ
print data

#update ����һ���ֵ������һ���ֵ�
d={"x":1}
e={"y":2}
e.update(d)
print d
print e


#values
d={"x":1,"y":2,"z":3}
print d.values()#��ӡ�ֵ���� ֵ
print list(d.itervalues())#��ӡ�ֵ���� ֵ �ĵ�����
'''
#������
'''
x=2
y=3
x,y=y,x#ֱ�ӽ���x y��ֵ
print x
print y

#if else elif 
num=raw_input("Enter a num:")
num=int(num) #raw_input()�����ַ����ķ�ʽ��ȡ�ģ�����Ҫת���� int,�������ֱ���� num=input("Enter a num:")���Ͳ���ת����
if num<0:
    print"���������С��0"
elif 0<num<100:
    print"�����������100����"
else:
    print"���������������:",num

for x in range(99,0,-1):
    root=sqrt(x)
    if root==int(root):
        print"100����ƽ������:",x
        break
else:
    print"Did't find it"
'''
'''
print [x*x for x in range(10)]#�б��Ƶ�ʽ��������ѭ��
print [x*x for x in range(10) if x%3==0]#�����ֿ�������3ʱ�����Ǽ������� ƽ����
print [(x,y)for x in range(3) for y in range(3)]#��ͬ��������⼸��
result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print resultresult=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print result

name=raw_input("��������:")
if name=="lili":
    print"lili"
elif name=="С��":
    pass#python�пմ����ǲ������ģ�������������һ�� pass
else:
    print"haha"
'''
'''
x=["hello","word"]
y=x
y[1]="python"#һЩֵ�ĸı�
print x
print y

#exec ִ��һ���ַ��������
score={}
exec"sqrt=1"in score
print sqrt(4)

#eval
print eval(raw_input("����һ������ʽ��"))#��ͣ�������2+5  

score={}
exec "x=2"in score
print eval("x*x",score) #����һ������ʽ
'''

#��6��
'''
fit=[0,1]
for x in range(8):
    fit.append(fit[-2]+fit[-1])
print fit
'''


#print tt.fitt(10)#���ﵼ�����tt.py�Ǹ�modle
'''
def try_to_change(n):
    n="Mr.Gumby"
name="Mrs Entity"
try_to_change(name)#n�������ֵ������û��Ӱ�쵽name������ֵ
print name

def change(n):
    n[0]="Mr Gumby"
names=["Mrs.Entity","Mrs white"]
change(names)#���ò�����names�б����ֵ�ı���
print names
'''
#6.4.2 Ϊʲô����Ҫ�޸Ĳ���
'''
storage={}
storage["first"]={}
storage["middle"]={}
storage["last"]={}
print storage #{'middle': {}, 'last': {}, 'first': {}}

me="Magnus Lie Hetland"
storage["first"]["Magnus"]=[me]
storage["middle"]["Lie"]=[me]
storage["last"]["Hetland"]=[me]
print storage #{'middle': {'Lie': ['Magnus Lie Hetland']}, 'last': {'Hetland': ['Magnus Lie Hetland']}, 'first': {'Magnus': ['Magnus Lie Hetland']}}

my_sister="Anne Lie Hetland"
storage["first"].setdefault("Ann",[]).append(my_sister)
storage["middle"].setdefault("Lie",[]).append(my_sister)
storage["last"].setdefault("Hetland",[]).append(my_sister)
print storage
print storage["first"]["Ann"]
print storage["middle"]["Lie"]

print "---------����������ķ�װ------------"
def init(data):
    data["first"]={}
    data["middle"]={}
    data["last"]={}

storage={}
init(storage)
print storage #{'middle': {}, 'last': {}, 'first': {}}

def lookup(data,lable,name):
    return data[lable].setdefault("lie","[Magnus Lie Hetland]")
print lookup(storage,"middle","Lie")
print storage
'''
'''
def print_params(*params):# *params����˼���ṩ�����
    print params
print_params("a","b","c") #('a', 'b', 'c')��ӡ��������Ԫ��

def print_params2(title,*params):
    print title,params
print_params2("myname",1,2,3) #��ӡ���� myname (1, 2, 3)

def print_params3(**params): #�����ؼ��ֲ���
    print params
print_params3(x=1,y=2,z=3) #��ӡ�������� �ֵ� {'y': 2, 'x': 1, 'z': 3}

def print_params4(x,y,z=3,*pos,**keypar): #�ۺϵ�һ��
    print x,y,z
    print pos
    print keypar
print_params4(1,2,3,4,5,6,fool=1,bar=2)

print"----------һ������-----------"
def init(data):
    data["first"]={}
    data["middle"]={}
    data["last"]={}
    
def lookup(data,lable,name):
    return data[lable].get(name)

def store(data,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2:
            names.insert(1,"")
        labels="first","middle","last"
        for label ,name in zip(labels,names):
            people=lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name]=[full_name]
d={}
init(d)
store(d,"a","c")
lookup(d,"last","ann")
print d
'''
'''#һ����ϰ
def s_with(**p):
    print p["name"],"is",p["age"]
x={"name":"lili","age":40}
s_with(**x)
'''
'''
def story(**kwy): #��һ������
    print"There is a %(L)s,named %(N)s" %kwy

def power(x,y,*other): #�ڶ�������
    if other:
        print"����Ĳ����ǣ�",other
    return pow(x,y)
def interval(start,stop=None,step=1): #����������
    if stop is None: #�ж�����ڶ����������Ϊ��
        start,stop=0,start #��start��Ϊ0��stopΪ������Ǹ���ֵ
    result=[]
    while start<stop:
        result.append(start)
        start+=step
    return result

story(L="language",N="python") #��һ������,��Ĭ��ֵ�ķ�ʽ��ֵ
params={"L":"object","N":"door"}
story(**params) #��һ�����������ֵ����ʽ��ֵ

p=(5,)*2 #�ڶ��������������ӡ��p����ʾ����(5,5)
print power(*p)
print power(x=2,y=3)
print power(5,2)
print power(3,3,"hello") #�����other������� 

print interval(10) #��� stop=None �����
print interval(2,6)#������ step=1
print interval(3,12,4) #���������� ������ step=4

print power(*interval(3,7))
'''
'''
def digui(n): #�ݹ�
    if n==1:
        return 1
    else:
        return n*digui(n-1)
print digui(3)

#map �������е�Ԫ��ȫ�����ݸ�һ������
print map(str,list("123456"))

g=lambda x:x**2 #lambda����
print g(3)
print map(lambda x : x**2,range(5))
'''
#������
'''
#��
class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello Word,I am %s." %self.name
foo=Person()
bar=Person()
foo.setName("H")
bar.setName("L")

foo.greet()
bar.greet()

foo.name="K"
print foo.getName()


class Secretive:
    def __ina(self): #����__ �Ǳ�ʾ�����ڲ�����ʹ�ã�����ⲿ�޷�ʹ��
        print"you can't see me"
    def acc(self):
        print"see me"
        self.__ina()#�����ڲ�����ʹ���������
s=Secretive()
#s.__ina() #����Ǵ����,��Ϊ����__�� �������ֻ�����������ʹ��
s.acc()
'''
'''
class MemberCounter:
    member=0
    def init(self):
        MemberCounter.member +=1
        
m1=MemberCounter()
m1.init()
print MemberCounter.member

m2=MemberCounter()
m2.init()
print MemberCounter.member

#ָ������
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return[x for x in sequence if x not in self.blocked]
class SPAM(Filter): #���ָ���˳��࣬SPAM��Filter��һ������
    def init(self): #��д�����е�init����
        self.blocked=["SPAM"]
s=SPAM()
s.init()
print s.filter(["SPAM","egg","SPAM","apple"])#���ݷ�����������SPAM

class Cla:
    def cla(self,exp):
        self.value=eval(exp)
class Talker:
    def talker(self):
        print "The value is: ",self.value

class TalkerCla(Cla,Talker): #ָ��������������,��Ϊ���ؼ̳�
    pass #ʲôҲû�ɣ�ֱ�ӹ�
tc=TalkerCla() 
tc.cla("1+2*4") #����ʲô��û�ɣ�ֱ�ӵ��ø���ķ���
tc.talker()
'''
#��8�£��쳣
'''
try:
    x=int(raw_input("first num:"))
    y=int(raw_input("second num:"))
    print x/y
except ZeroDivisionError:
    print"The second num can't be Zero"


class Muff: #��ΪFalse���δ�ӡ����ΪTrue������Ҫ��ӡ����Ϣ���Լ������ж�� except
    muf=False
    def cal(self,exp):
        try:
            return eval(exp)
        except ZeroDivisionError:
            if self.muf: 
                print"num can't be Zero"
            else:
                raise Exception("something is wrong")
        except TypeError:
            print"wasn't a number"
m=Muff()
print m.cal("10/2")
m.muf=True
m.cal("10/0")
m.cal("10/'a'")

#�� try except �Ӹ� else 
while True: #ֻҪ�д����һֱ��ʾ���룬����������ȷ�����˳�
    try:
        x=int(raw_input("first num:"))
        y=int(raw_input("second num:"))
        value=x/y
        print "x/y is:",value
    except Exception,e:
        print "Invalid input",e
        print "Please try again"
    else:
        break
'''   
#��9��
'''
class FooBar:
    def __init__(self): #���캯�� 
        self.some=42
    def name(self):
        self.m="my"
f=FooBar()
print f.some

class FooBar1:
    def __init__(self,value=42): #���캯�������Ӳ���
        self.some1=value
f1=FooBar1("this is argument")
print f1.some1
'''

'''
#��дһ��ķ���������Ĺ��췽��
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print"I an full"
            self.hungry=False
        else:
            print"No,Thinks"
class SongBird(Bird): #ָ������
    def __init__(self):
        self.sound="Squawk"
    def sing(self):
        print self.sound
sBird=SongBird()
sBird.sing()

SongBird()ָ����Bird Ϊ���࣬���ֱ�ӵ��ø�����ķ����ᱨ������Ϊ SongBird()�� ���췽������д�����µĹ��췽��û���κι��ڳ�ʼ��
hungry���ԵĴ���,���������

#sBird.eat()#����Ǵ����
#�����ǽ�����������������ַ���
class Bird1:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print"I an full"
            self.hungry=False
        else:
            print"No,Thinks"
class SongBird1(Bird1): #ָ������
    def __init__(self):
        Bird1.__init__(self) #������һ�䣬����Ϊ����һ��ʵ���ķ���ʱ���÷�����self�����ᱻ�Զ��󶨵�ʵ����
        self.sound="Squawk"
    def sing(self):
        print self.sound
sBird1=SongBird1()
sBird1.sing()
sBird1.eat()#��ؾ�û����
sBird1.eat()#��ؾ�û����

#ʹ�� super()����
class Bird2(object): #֮��ʹ��superʱ������Ҫ����object
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print"I an full"
            self.hungry=False
        else:
            print"No,Thinks"
class SongBird2(Bird2): 
    def __init__(self):
        super(SongBird2,self).__init__() #super����
        self.sound="Squawk"
    def sing(self):
        print self.sound
sBird2=SongBird2()
sBird2.sing()
sBird2.eat()#��ؾ�û����
sBird2.eat()#��ؾ�û����
'''
'''
class Rect:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name=="size":
            self.height,self.width=value
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        if name=="size":
            return self.height,self.width
        else:
            raise AttributeError
r=Rect()
print r.width,r.height
r.__setattr__("size", "na")
print r.width,r.height
'''
#����
'''
lst=range(3)
it = iter(lst)
print it.next() #������ next(it)Ч����һ����
print it.next()

try:
    while True:
        var=it.next()
        print var
except Exception, e:
    print e
    
    
it=iter([1,2,3])#һ������
print it.next()

#һ������������
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        
        print self.a
        print self.b
        
        return self.a
    def __iter__(self):
        return self
fibs=Fibs()
for f in fibs:
    if f>3:
        print "ѭ�����ֵΪ:",f
        break

#������ yield
nested=[[1,2],[3,4],[5,6]]
def Flatten(nested):
    for sublist in nested:
        for ele in sublist:
            yield ele  #�κΰ���yield���ĺ�����Ϊ ������
nested1=[[1,2],[3,4],[5,6]]
for num in Flatten(nested1):
    print num
print list(Flatten(nested1))#����һ������


# ��178-183 �˻ʺ����� û����
'''
'''
#��10��
print time.localtime()
print random.random()#����0-1��ֵ
print random.randrange(1,10) #�Ӹ����ķ�Χ�����ȡֵ
print random.randrange(1,20,2) #���20���ڵ��� ����

some="alpha,beta,,,,gamma,delta"
print re.split("[,]+", some) #����ƥ����ָ��ַ���

pat="[a-zA-Z]+"
text="asdf...asdfdxzxcvm,"
print re.findall(pat,text)#���ַ����в���˵�еĵ���

pat=r"[.?\-',]+"
text=",./jlk?lk;\l"
print re.findall(pat,text)#���ұ�����

import fileinput #�ܱ����ı��е�������
for line in fileinput.input(inplace=True):
    line=line.rstrip #ȥ�����˵Ŀո�
    num=fileinput.lineno() #���ص�ǰ�ۼƵ�����
    print"%-40s # %2i" %(line,num)
'''

#��11��
'''
f=open(r"./something/test.txt","w") #���ļ��н��� д �Ĳ�����   ./test.txt ��˵�������Ŀ�ĸ�Ŀ¼��
f.write("hello\n") 
f.write("ss\n")
f.write("word1\n")
f.close()

f=open(r"./something/test.txt","r")# ���ļ��н��� �� �Ĳ���
print f.read()#��ȡ�����ļ�
#print f.read(5)#��4���ַ�
f.close

print"-----------"
f=open(r"./something/test.txt","r")# ���ļ��н��� �� �Ĳ���
#print f.readline()#��ȡһ��
for line in f.readlines():#f.readlines()ÿһ�ж� ��ȡ��   f.readline()ֻ��ȡһ��
    print line

f.close

print"-----------" #�޸�ĳһ�е���Ϣ
f=open(r"./something/test.txt","r")# ���ļ��н��� �� �Ĳ���
re=f.readlines()
f.close()
re[1]="WW\n"#���±�Ϊ���������Ϣ�޸�Ϊ WW


f=open(r"./something/test.txt","w")
f.writelines(re)#�� �ļ���д��
f.close()

f=open(r"./something/test.txt","r")
print f.read()
'''

#���ļ����ݽ��е���
def process(string):
    print string
'''
f=open(r"./something/mytext.txt") #��ӡ��ÿ���ַ�����ʾ
char=f.read(1) 
while char:
    process(char)
    char=f.read(1)
f.close()

c=[]
f=open(r"./something/mytext.txt") 
for char in f.read():
    c.append(char)
print len(c)  #��������ļ����ж����ַ�
f.close()

f=open(r"./something/mytext.txt") 
for line in f.readlines():
    process(line)
f.close()

lines=list(open(r"./something/mytext.txt")) #���ļ������Ϣ���ӵ� ����
print lines
'''
#��12��GUI
'''
��װwxPython2.8-win32-unicode-2.8.12.1-py27ʱ
Ҫ��  windows->Preferences->PyDev->Interpreter - Python-Libraries������
Python27\Lib\site-packages\wx-2.8-msw-unicode Ŀ¼��ǿ�Ʊ���(Apply)���ɣ�һ��Ҫ���Apply��ok������eclipse�Ϳ�����
'''
'''
import wx
def load(event):#С�������Ҳ���ǵ����open����ť
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
def save(event):
    file=open(filename.GetValue(),"w")
    file.write(contents.GetValue())
    file.close()
app=wx.App()
win=wx.Frame(None,title="ok python",size=(410,335))
bkg=wx.Panel(win)

loadbtn=wx.Button(bkg,label="Open")
loadbtn.Bind(wx.EVT_BUTTON,load)#�����ť��Ĵ�������
    
savebtn=wx.Button(bkg,label="Save")
savebtn.Bind(wx.EVT_BUTTON,save)#�����ť��Ĵ�������

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savebtn,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
'''
#��13�� �һ����ϵ�mysql name��MySQL��root���룺123456
'''
import MySQLdb ʱ��ʾ��unresolved import:MYSQLdb
��Ҫ��PyDev����֧�֣�
�򿪣�windows->Preferences->PyDev->Interpreter - Python
��Forced Builtins�����ֹ����� MySQLdb �ֶ� ǿ�Ʊ��롣
Apply֮�󣬿��Կ��� Libraries ���������� MySQLdb��Ŀ¼�����û�У����ֹ���Libraries 
��������MySQLdb��Ŀ¼���ٴ�ǿ�Ʊ���(Apply),���ok������
'''
'''
import mysqldbtest
mysqldbtest.createdb()#�������ݿ�
mysqldbtest.operateDatabase()#�����ݿ����������
#�������������ӣ�http://www.cnblogs.com/rollenholt/archive/2012/05/29/2524327.html 
#http://www.iteye.com/topic/573092
'''
#��14�� �ÿ�266�� �����Ȳ�ע��socket������������һ��
'''
import socket
#һ��С�ͷ�����
s=socket.socket()
host=socket.gethostname()
print host #��ӡ���Լ��ļ������ host����
port=12345
s.bind((host,port))
s.listen(5)#ֻ��һ����������������δ���������ӵĳ��ȣ��������Ŷӵȴ���������Ŀ����Щ������ֹͣ����֮ǰ�ȴ����գ�
while True:
    c,addr=s.accept()#���������׽��ֿ�ʼ���������Ϳ��Խ��տͻ��˵����ӡ����������accpet���������,��һ��Ԫ��c���µ�socket���󣬷���������ͨ������ͻ�ͨ�ţ��ڶ���Ԫ�� addr�ǿͻ���Internet��ַ��
    print"Got connecting from",addr
    c.send("Thinking you for connecting")#����ʹ���ַ�����������send�Է�������
    c.close()

#һ��client
s1=socket.socket()
host1=socket.gethostname()
port1=12345
s1.connect((host1,port1))#�ͻ����׽���ʹ��connect�������ӵ�������
print s1.recv(1024)#��һ������ģ�����ֽ������������� recv����������
'''

'''
#��Զ���ļ�
from urllib import urlopen
print urlopen("http://www.baidu.com")#����һ�����ӵ�http://www.baidu.com��ҳ�����ļ�����
print "--"*20
#��һ������ ��ȡ���е�����
webpage=urlopen("http://www.baidu.com").read()
print webpage

print "--"*20
#��ȡhttpͷ
doc=urlopen("http://www.baidu.com")
print doc.info()
print "--"*20
print doc.info().getheader("Content-Type")

#��ȡԶ���ļ�
import urllib
#urlretrieve  �����ļ������ڱ����ļ��д洢һ���ļ��ĸ���
urllib.urlretrieve("http://www.baidu.com",r"./something/baidu_webpage.html")
�ÿ�266��
'''
#��15��,��һ������ĳ��򿴵Ĳ�̫��
'''
from subprocess import Popen,PIPE
text=open(r"./something/mxTidy.html").read()
tidy=Popen("tidy",stdin=PIPE,stdout=PIPE,stderr=PIPE)
tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read() #������򱨴�
'''
'''
#ʹ��HTMLParserץȡ��Ļ��Ϣ
from urllib import urlopen
from HTMLParser import HTMLParser
class Scraper(HTMLParser):
    in_h3=False
    in_link=False
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=="h3":
            self.in_h3=True
        if tag=="a" and "href" in attrs:
            self.in_link=True
            self.chunks=[]
            self.url=attrs["href"]
        print attrs
    def handle_data(self,data):
        if self.in_link:
            self.chunks.append(data)
    def handle_endtag(self,tag):
        if tag=="h3":
            self.in_h3=False
        if tag=="a":
            if self.in_h3 and self.in_link:
                print"%s(%s)"%(''.join(self.chunks),self.url)
            self.in_link=False
text=urlopen("http://www.sina.com").read()
parser=Scraper()
parser.feed(text)#����feed�������������������
parser.close()
'''
#��16��
#�� my_math module



''' 
#һ��С�㷨
#foo(A,B,C)
#���ҳ�A����B��ͷ����C��β�������ַ���

def foo(A,B,C):
    for x in A:
        if x[0]==B and x[-1]==C:
            print x
A=["BsC","BafaC","dfg"]
foo(A,"B","C")
'''


'''
#���ʵ�ֶ���������A���ҳ�����3����֮�����Ĳ��֣�����Ʋ����������Ըú��������磺
#A = [2, -3, 5, 0, 6, -4]�����ֵΪ11

def maxNum(A):
    temp=[]
    for x in range(len(A)-2):
        temp.append(A[x]+A[x+1]+A[x+2])
    print max(temp)
    
A = [2, -3, 5, 0, 6, -4]
#maxNum(A)
'''
'''
#��17��
#��21�� ��Drawing module
import Drawing
Drawing.draw()
print"��ִ����ϣ��뵽  ��Ŀ¼�²鿴 report.pdf"
'''

#��26��

'''419'''
'''420'''