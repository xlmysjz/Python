#-*-coding:utf-8-*-
#Python����������� ���鼮

print"ni"\
     "hao"

#������ ����ȫ�ֱ����� �������ȫ�ֱ���
_a=2
_b=3
def add():
    global _a#���������ȫ�ֱ��� _a
    _a=5
def sub():
    global _b #���������ȫ�ֱ��� _b
    return _a - _b
if __name__=="__main__":
    add()
    print sub()
    
    print not 1