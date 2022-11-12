# -*- coding: UTF-8 -*-
import numpy as np
from math import sqrt

random = np.random.choice([0,1,3,4],2000)

x,y = 0,0

for i in random:
    if i == 1:
        x = x+0.5
    elif i == 2:
        x = x-0.5
    elif i == 3:
        y = y+0.5
    else:
        y = y-0.5

coordinate = (x,y)
print(coordinate[0],coordinate[1])
def vector(v):
    return sqrt(v[0]**2+v[1]**2)

jg_length = vector(coordinate)

print("酒鬼离原点距离:",jg_length)