# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 下午2:02
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : Jaccard_distance.py
# @Software: PyCharm
import numpy as np
import scipy.spatial.distance as dist
def Jac_dis_1(a,b):
    #with scipy
    a=np.array(a)
    b=np.array(b)
    tmp_mat=np.array([a,b])
    return dist.pdist(tmp_mat,'jaccard')[0]



if __name__ == '__main__':
    li1=[1,2,3,4]
    li2=[1,2,6,7]
    print(Jac_dis_1(li1,li2))

