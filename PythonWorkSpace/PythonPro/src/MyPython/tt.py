'''
Created on 2013-4-16

@author: Administrator
'''

def fitt(num):
    result=[0,1]
    for x in range(num-2):
        result.append(result[-2]+result[-1])
    return result

