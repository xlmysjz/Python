#-*-coding:utf-8-*-
#Python开发技术祥解 的书籍

#使用字典模拟 switch
x=6
y=2
operator="/"
result={
        "+":x+y,
        "-":x-y,
         "*":x*y,
          "/":x/y }
print result.get(operator)

#冒泡排序
def maoPaoSort(num):
    for x in range(len(num)-1,-1,-1):
        for y in range(x):
            if num[y]>num[y+1]:
                num[y],num[y+1]=num[y+1],num[y]
            print num
                
num=[23,11,56,9,8]
maoPaoSort(num)