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
names=[d[0] for d in curs.description]#names取的是数据库中的每个字段名称

rows=[dict(zip(names,row)) for row in curs.fetchall()]#将字段名称跟字段里的数据想对应，并形成一个字典
print rows #可以把这个注释掉
toplevel=[]
children={}

for row in rows:
    parent_id=row["reply_to"]
    print parent_id #可以注释掉
    if parent_id is None:
        toplevel.append(row)
    else:
        children.setdefault(parent_id,[]).append(row)
print children #可以注释掉

def format():
    print'<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>'%row
    try:
        kids=children[row["id"]]
        print kids #可以注释掉
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
def createTable():#创建数据库见 mysqldatest 模块
    conn=MySQLdb.Connect(host="127.0.0.1",user="root",passwd="123456")
    curs=conn.cursor()
    conn.select_db("python")
    
    count=curs.execute(""" Create table messages
                        (id INT NOT NULL AUTO_INCREMENT,
                        subject VARCHAR(100) NOT NULL, #主题字符串
                        sender VARCHAR(15) NOT NULL, #包括发送者名字 email地址或其他信息
                        reply_to INT,
                        text MEDIUMTEXT NOT NULL, #内容字段
                        PRIMARY KEY(id))""")
    
'''    
    
    
    
if __name__=="__main__":
    #createTable()
#420