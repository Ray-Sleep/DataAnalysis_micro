# -*- coding: UTF-8 -*-
"""
@Project :DataAnalysis_micro 
@File    :report1.py
@Author  :李睡睡 主人
@Date    :2022/11/12 17:22 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import numpy as np
import csv

iris_data = []
with open("iris.csv") as csvfile:
    # 使用 csv.reader 读取 csvfile 中的文件：
    csv_reader = csv.reader(csvfile)

    # 读取第一行各列的标题
    birth_header = next(csv_reader)
    # 将 csv 文件中的数据保存到 birth_data 中
    for row in csv_reader:
        iris_data.append(row)

iris_list = []
for row in iris_data:
    iris_list.append(tuple(row[1:]))

datatype = np.dtype([("Sepal.Length",np.str_,40),
                     ("Sepal.Width",np.str_,40),
                     ("Petal.Length",np.str_,40),
                     ("Petal.Width",np.str_,40),
                     ("Species",np.str_,40)])

iris_data = np.array(iris_list,dtype = datatype)

PetalLength = iris_data["Petal.Length"].astype(float)

sort_PetaLength = np.sort(PetalLength)
print("指定列的排序：",sort_PetaLength)

uni_PetalLength = np.unique(PetalLength)
print("指定列的去重：",uni_PetalLength)

# 和：
sum_PL = np.sum(PetalLength)
print("指定列的和：",sum_PL)

# 均值：
mean_PL = np.mean(PetalLength)
print("指定列的均值：",mean_PL)

# 标准差
std_PL = np.std(PetalLength)
print("指定列的标准差：",std_PL)

# 方差
var_PL = np.var(PetalLength)
print("指定列的方差：",var_PL)

# 最小值
min_PL = min(PetalLength)
print("指定列的最小值：",min_PL)

# 最大值
max_PL = max(PetalLength)
print("指定列的最大值：",max_PL)
