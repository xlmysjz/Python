#-*-coding:utf-8-*-
'''
����һ�� ��д�ű� �ٵ� ���Խű�������
'''
class myscript:
    #һ��С�㷨
    #foo(A,B,C)
    #���ҳ�A����B��ͷ����C��β�������ַ���
    #A=["BsC","BafaC","dfg"]
    def __init__(self):
        pass
    def foo(self,A,B,C):
        list=[]
        for x in A:
            if x[0]==B and x[-1]==C:
                list.append(x)
        return list
        
        #���ʵ�ֶ���������A���ҳ�����3����֮�����Ĳ��֣�����Ʋ����������Ըú��������磺
        #A = [2, -3, 5, 0, 6, -4]�����ֵΪ11
    def maxNum(self,A):
        temp=[]
        for x in range(len(A)-2):
            temp.append(A[x]+A[x+1]+A[x+2])
        return max(temp)


