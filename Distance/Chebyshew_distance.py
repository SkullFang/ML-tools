# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 下午1:33
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Chebyshew_distance.py
# @Software: PyCharm
import numpy as np
def Che_dis_1(a,b):
    a = np.array(a)
    b = np.array(b)
    return np.abs(a-b).max()

def Che_dis_2(a,b):
    a = np.array(a)
    b = np.array(b)
    return np.linalg.norm(a-b,ord=np.inf)

if __name__ == '__main__':
    li1=[1,2,3]
    li2=[4,5,6]
    print(Che_dis_1(li1,li2)) #3
    print(Che_dis_2(li1,li2))

