# -*- coding: UTF-8 -*-
import numpy as np

def jiuguimanbu(t):
    vector = np.random.choice([0, 1], t)
    to_zero = (vector == 0)
    vector[to_zero] = -1
    # 使用cumsum()函数步数累计和，显示酒鬼每一步距原点的距离
    cum_sum = vector.cumsum() * 0.5
    return cum_sum[-1]

t = int(input("请输入酒鬼行进的步数(时刻)："))
test = jiuguimanbu(t)
print(test,"m")

