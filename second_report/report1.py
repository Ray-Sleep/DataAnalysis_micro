# -*- coding: UTF-8 -*-
"""
@Project :DataAnalysis_micro 
@File    :report1.py
@Author  :李睡睡 主人
@Date    :2022/11/26 10:37 
@Scripts :pandas numpy matplotlib.pyplot
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# % matplotlib inline

fdata = pd.read_excel('tips.xls')

print("=============表头数据=============")
print(fdata.head())

print("=============数据描述信息=============")
print(fdata.describe())

print("=============修改列名为汉字，并显示前5行数据=============")
fdata.rename(columns={'total_bill':'消费总额','tip':'小费','sex':'性别','smoker':'是否抽烟','day':'星期','time':'聚餐时间段','size':'人数'},inplace = True)
print(fdata.head())

print("=============分析小费金额和总金额=============")
fdata.plot(kind='scatter',x='消费总额',y='小费')
plt.suptitle('分析小费金额和总金额')
plt.show()

print("=============分析男性顾客和女性顾客谁更慷慨=============")
ans = fdata.groupby('性别')['小费'].mean()
print(ans)

print("=============分析日期和小费的关系=============")
print(fdata['星期'].unique()) # 显示星期的取值
r = fdata.groupby('星期')['小费'].mean()
fig = r.plot(kind='bar',x='星期',y='小费',fontsize=12,rot=30)
fig.axes.title.set_size(16)
plt.suptitle('分析日期和小费的关系')
plt.show()

print("=============性别+抽烟的组合因素对慷慨度的影响=============")
r = fdata.groupby(['性别','是否抽烟'])['小费'].mean()
fig = r.plot(kind='bar',x='星期',y='小费',fontsize=12,rot=30)
fig.axes.title.set_size(16)
plt.suptitle('性别+抽烟的组合因素对慷慨度的影响')
plt.show()

print("=============分析聚餐时间段与小费数额的关系=============")
r = fdata.groupby(['聚餐时间段'])['小费'].mean()
fig = r.plot(kind='bar',x='星期',y='小费',fontsize=12,rot=30)
fig.axes.title.set_size(16)
plt.suptitle('分析聚餐时间段与小费数额的关系')
plt.show()
