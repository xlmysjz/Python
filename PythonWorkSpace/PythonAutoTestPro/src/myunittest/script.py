#-*-coding:utf-8-*-
'''
这是一个 从写脚本 再到 测试脚本的例子
'''
class myscript:
    #一个小算法
    #foo(A,B,C)
    #请找出A中以B开头，以C结尾的所有字符串
    #A=["BsC","BafaC","dfg"]
    def __init__(self):
        pass
    def foo(self,A,B,C):
        list=[]
        for x in A:
            if x[0]==B and x[-1]==C:
                list.append(x)
        return list
        
        #编程实现对整数数组A，找出连续3个数之和最大的部分，并设计测试用例测试该函数。例如：
        #A = [2, -3, 5, 0, 6, -4]，最大值为11
    def maxNum(self,A):
        temp=[]
        for x in range(len(A)-2):
            temp.append(A[x]+A[x+1]+A[x+2])
        return max(temp)


