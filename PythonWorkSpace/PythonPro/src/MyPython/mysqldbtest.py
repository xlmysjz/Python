#-*-coding:utf-8-*-
'''
Created on 2013-5-3

@author: Administrator
'''
import MySQLdb
def createdb():#����һ�����ݿ����ӣ�������һ�����ݿ�
    #�������ݿ����� ע��hostҪд127.0.0.1�����д localhoat�ᱨ��
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',charset="gbk")
    curs = conn.cursor()#��ȡ�����α�
    curs.execute("""create database python """)#�������ݿ⣬����Ϊpython
    print"�������ݿ�ɹ�"
    curs.close()#�ر����ӣ��ͷ���Դ

def operateDatabase():#�������������ݣ�����������ݣ����޸����һ������
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456")
    curs=conn.cursor()#��ȡ�����α�
    curs.execute(""" create database if not exists python""" )#�������������Ϊ python�����ݿ⣬�ʹ���.
    
    conn.select_db("python")#ѡ�����ݿ�
    
    curs.execute("""create table pythontest(id int PRIMARY KEY,
                    recoder char(50),
                    info varchar(50))""")
    value=[1,"nan","name"]
    curs.execute("Insert into pythontest Values(%s,%s,%s)",value)#����һ������
    
    #�����������
    values=[]
    for i in range(2,10):
        values.append((i,"recoder"+str(i),"name"+str(i)))
    curs.executemany("Insert into pythontest Values(%s,%s,%s)",values)
    
    #�����޸�һ������
    curs.execute("""Update pythontest Set recoder="recoder1"Where id=1""")
    
    #�в��롢���µȵĲ��� һ��Ҫcommit�����򲻻����Ч
    conn.commit()
    
    #��ѯ���
    count=curs.execute("Select * From pythontest")
    print "there has %s rows records" %count
    
    #ֻ��ȡһ����¼
    result=curs.fetchone()
    print result
    print "ID:%s,recoder:%s,info%s" %result
    
    print"��ȡ5����¼"+"--"*20
    #��ȡ5����¼��ע������֮ǰִ������fetchone()�������α��Ѿ�ָ���ڶ�����¼�ˣ�Ҳ���Ǵӵڶ�����ʼ�����м�¼ 
    results=curs.fetchmany(5)
    for r in results:
        print r
        print "ID:%s,recoder:%s,info%s" %r
        
    print"��ȡȫ����¼"+"--"*20
    #��ȡ���н��
    curs.scroll(0,mode="absolute")#�����α�λ�ã�0,Ϊƫ������mode��absolute | relative,Ĭ��Ϊrelative
    allResults=curs.fetchall()
    for r in allResults:
        print r #�ĳ� print r[1]����
       
    curs.close()#�ر����ӣ��ͷ���Դ
    conn.close()#�ر��������ݿ�
if __name__ =="__main__":
    createdb()
    operateDatabase()
