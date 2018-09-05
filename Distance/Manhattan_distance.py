# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 下午1:24
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Manhattan_distance.py
# @Software: PyCharm
import numpy as np
def Man_dis_1(a,b):
    a=np.array(a)
    b=np.array(b)
    return np.sum(np.abs(a-b))

def Man_dis_2(a,b):
    a=np.array(a)
    b=np.array(b)
    return np.linalg.norm(a-b,ord=1)

def Man_dis_3(a,b):
    #mat
    a=np.mat(a)
    b=np.mat(b)
    return np.sum(np.abs(a-b)).tolist()

if __name__ == '__main__':
    li1=[1,2,3]
    li2=[4,5,6]
    print(Man_dis_1(li1,li2))
    print(Man_dis_2(li1,li2))
    print(Man_dis_3(li1,li2))