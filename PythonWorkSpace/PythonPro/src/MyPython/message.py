#-*-coding:utf-8-*-
'''
Created on 2013-5-21

@author: Administrator
'''
import MySQLdb
print"Content-type:text/html\n"
import cgitb; cgitb.enable()

conn=MySQLdb.Connect(host="127.0.0.1",user="root",passwd="123456")
curs=conn.cursor()
conn.select_db("python")

print"""
<html>
    <head>
        <title>The FooBar Bulletin Board</title>
    </head>
    <body>
        <h1>The FooBar Bulletin Board<h1>
    """


curs.execute("SELECT * From messages")
names=[d[0] for d in curs.description]#namesȡ�������ݿ��е�ÿ���ֶ�����

rows=[dict(zip(names,row)) for row in curs.fetchall()]#���ֶ����Ƹ��ֶ�����������Ӧ�����γ�һ���ֵ�
print rows #���԰����ע�͵�
toplevel=[]
children={}

for row in rows:
    parent_id=row["reply_to"]
    print parent_id #����ע�͵�
    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id,[]).append(row)
print children #����ע�͵�

def format():
    print'<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>'%row
    try:
        kids=children[row["id"]]
        print kids #����ע�͵�
    except KeyError:
        pass
    else:
        print"<blockquote>"
        for kid in kids:
            format(kid)
        print"</blockquote>"
print"<p>"
for row in toplevel:
    format(row)
print"""
        </p>
        <hr />
        <p><a href="edit.cgi">Post message</a></p>
    </body>
    </html>
    """

'''
def format():
    print'<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>'%row
def createTable():#�������ݿ�� mysqldatest ģ��
    conn=MySQLdb.Connect(host="127.0.0.1",user="root",passwd="123456")
    curs=conn.cursor()
    conn.select_db("python")
    
    count=curs.execute(""" Create table messages
                        (id INT NOT NULL AUTO_INCREMENT,
                        subject VARCHAR(100) NOT NULL, #�����ַ���
                        sender VARCHAR(15) NOT NULL, #�������������� email��ַ��������Ϣ
                        reply_to INT,
                        text MEDIUMTEXT NOT NULL, #�����ֶ�
                        PRIMARY KEY(id))""")
    
'''    
    
    
    
if __name__=="__main__":
    #createTable()
#420