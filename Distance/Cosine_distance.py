# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 下午1:47
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Cosine_distance.py
# @Software: PyCharm
import numpy as np
def Cos_dis_1(a,b):
    a=np.array(a)
    b=np.array(b)
    fenzi=np.dot(a,b)
    fenmu=np.linalg.norm(a)*np.linalg.norm(b)#模
    return fenzi/fenmu

if __name__ == '__main__':
    li1=[1,2,3]
    li2=[4,7,5]
    print(Cos_dis_1(li1,li2))