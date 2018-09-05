# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 上午10:31
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Euclidean_distance.py
# @Software: PyCharm
import numpy as np
def Euc_dis_1(a,b):
    a=np.array(a)
    b=np.array(b)
    #1
    re1=np.sqrt(np.sum(np.square(a-b)))
    return re1

def Euc_dis_2(a,b):
    #np.linalg.norm
    a=np.array(a)
    b=np.array(b)
    re2=np.linalg.norm(a-b)
    return re2

def Euc_dis_3(a,b):
    a=np.array(a)
    b=np.array(b)
    re3=np.sqrt((a-b).dot((a-b).T))
    return re3

def Euc_dis_4(a,b):
    #with mat
    a=np.mat(a)
    b=np.mat(b)
    re4=np.sqrt((a-b)*(a-b).T).tolist()
    return re4[0][0]

if __name__ == '__main__':
    li1=[1,2,3]
    li2=[4,5,6]
    print(Euc_dis_1(li1,li2))
    print(Euc_dis_2(li1,li2))
    print(Euc_dis_3(li1,li2))
    print(Euc_dis_4(li1,li2))