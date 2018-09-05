# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 下午1:54
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Hamming_distance.py
# @Software: PyCharm
import numpy as np
def Ham_dis_1(a,b):
    a=np.array(a)
    b=np.array(b)
    tmp=np.nonzero(a-b)
    return np.shape(tmp)[1]


if __name__ == '__main__':
    li1=[1,1,0,1,0,1,0,0,1]
    li2=[0,1,1,0,0,0,1,1,1]
    print(Ham_dis_1(li1,li2))