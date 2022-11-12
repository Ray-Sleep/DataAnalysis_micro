# -*- coding: UTF-8 -*-
import numpy as np

a = np.zeros((8,8))
for i in range(8):
    if i % 2:
        for j in range(8):
            if j % 2:
                a[i][j] = 0
            else:
                a[i][j] = 1
    else:
        for j in range(8):
            if j % 2:
                a[i][j] = 1
            else:
                a[i][j] = 0
print(a)
