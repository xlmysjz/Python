#-*-coding:utf-8-*-
#Python开发技术祥解 的书籍

print"ni"\
     "hao"

#下面是 定义全局变量后 如何引用全局变量
_a=2
_b=3
def add():
    global _a#引用上面的全局变量 _a
    _a=5
def sub():
    global _b #引用上面的全局变量 _b
    return _a - _b
if __name__=="__main__":
    add()
    print sub()
    
    print not 1