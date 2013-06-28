#-*-coding:utf-8-*-
'''
Created on 2013-5-3

@author: Administrator
'''
import MySQLdb
def createdb():#建立一个数据库链接，并创建一个数据库
    #建立数据库链接 注意host要写127.0.0.1，如果写 localhoat会报错
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',charset="gbk")
    curs = conn.cursor()#获取操作游标
    curs.execute("""create database python """)#创建数据库，名称为python
    print"建立数据库成功"
    curs.close()#关闭链接，释放资源

def operateDatabase():#创建表，插入数据，插入多条数据，并修改最后一条数据
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456")
    curs=conn.cursor()#获取操作游标
    curs.execute(""" create database if not exists python""" )#如果不存在名称为 python的数据库，就创建.
    
    conn.select_db("python")#选择数据库
    
    curs.execute("""create table pythontest(id int PRIMARY KEY,
                    recoder char(50),
                    info varchar(50))""")
    value=[1,"nan","name"]
    curs.execute("Insert into pythontest Values(%s,%s,%s)",value)#插入一条数据
    
    #插入多条数据
    values=[]
    for i in range(2,10):
        values.append((i,"recoder"+str(i),"name"+str(i)))
    curs.executemany("Insert into pythontest Values(%s,%s,%s)",values)
    
    #更新修改一条数据
    curs.execute("""Update pythontest Set recoder="recoder1"Where id=1""")
    
    #有插入、更新等的操作 一定要commit，否则不会插生效
    conn.commit()
    
    #查询语句
    count=curs.execute("Select * From pythontest")
    print "there has %s rows records" %count
    
    #只获取一条记录
    result=curs.fetchone()
    print result
    print "ID:%s,recoder:%s,info%s" %result
    
    print"获取5条记录"+"--"*20
    #获取5条记录，注意由于之前执行有了fetchone()，所以游标已经指到第二条记录了，也就是从第二条开始的所有记录 
    results=curs.fetchmany(5)
    for r in results:
        print r
        print "ID:%s,recoder:%s,info%s" %r
        
    print"获取全部记录"+"--"*20
    #获取所有结果
    curs.scroll(0,mode="absolute")#重置游标位置，0,为偏移量，mode＝absolute | relative,默认为relative
    allResults=curs.fetchall()
    for r in allResults:
        print r #改成 print r[1]试试
       
    curs.close()#关闭链接，释放资源
    conn.close()#关闭连接数据库
if __name__ =="__main__":
    createdb()
    operateDatabase()
