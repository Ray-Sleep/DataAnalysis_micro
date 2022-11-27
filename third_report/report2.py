# -*- coding: UTF-8 -*-
"""
@Project :DataAnalysis_micro 
@File    :report2.py
@Author  :李睡睡 主人
@Date    :2022/11/27 21:13 
@Scripts :
@Documentation:
@Function:
@Tips    :不要左顾右盼。慢慢积累，慢慢写吧。毕竟除了这样单调的努力，我什么也做不了。
"""

#6.3  数据分析
import pandas as pd
df = pd.read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')
df.head()

df.数分.describe()   #查看“数分”列的基本统计
df.describe()  #所有各列的基本统计
df.解几.size   #注意：这里没有括号()
df.解几.size   #注意：这里没有括号()
df.解几.min()
df.解几.sum()
df.解几.mean()
df.解几.var()
df.解几.std()


import numpy as np
np.mean(df['数分'])

np.average(df['数分'])
df['数分'].mean()
df.median()
df.mode()


#6.3.2  分组分析
import numpy as np
from pandas import read_excel
df = read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')
df

df.groupby('班级')[['军训','英语','体育', '性别']].mean()
df.groupby(['班级', '性别'])[['军训','英语','体育']].mean()   #by=可省略不写



df2 = df.groupby(by=['班级','性别'])['军训'].agg([('总分',np.sum),
                                      ('人数',np.size),
                                      ('平均值',np.mean),
                                      ('方差',np.var),
                                      ('标准差',np.std),
                                      ('最高分',np.max),
                                      ('最低分',np.min)])

df2 = df.groupby(by=['班级','性别'])['军训'].agg([np.sum,
                                      np.size,
                                      np.mean,
                                      np.var,
                                      np.std,
                                      np.max,
                                      np.min]).rename(
                                         columns={'sum': '总分',
                                                  'size':'人数',
                                                  'mean':'平均值',
                                                  'var':'方差',
                                                  'std':'标准差',
                                                  'amax':'最高分',
                                                  'amin':'最低分'})

df.groupby(['班级','性别']).agg(
                                 {'军训':[np.sum,
                                           np.size,
                                           np.mean,
                                           np.var,
                                           np.std,
                                           np.max,
                                           np.min]}).rename(
                                               columns={'sum': '总分',
                                                     'size':'人数',
                                                     'mean':'平均值',
                                                     'var':'方差',
                                                     'std':'标准差',
                                                     'amax':'最高分',
                                                     'amin':'最低分'})




df2.xs(23080242) #注意班级号的数据类型，若是文本型则需要加引号

df2.groupby("最低分").apply(lambda x:x.sort_values("最低分", ascending=False))

#6.3.3  分布分析
import pandas as pd
import numpy
from pandas import read_excel
df = pd.read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')
df.head()

df['总分']=df.英语+df.体育+df.军训+df.数分+df.高代+df.解几
df['总分'].head()
df['总分'].describe()
bins = [min(df.总分)-1,400,450,max(df.总分)+1]   #将数据分成三段
bins

labels=['400及其以下','400到450','450及其以上']  #给三段数据贴标签
labels

总分分层 = pd.cut(df.总分,bins,labels=labels)
总分分层.head()

df['总分分层']= 总分分层
df.tail()

df.groupby(by=['总分分层']).agg({'总分':np.size}).rename(columns={"总分":'人数'})


#6.3.4  交叉分析
import pandas as pd
import numpy
from pandas import pivot_table
from pandas import read_excel
df = pd.read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')
df.pivot_table(index=['班级','姓名'])

df.pivot_table(['军训','英语','体育', '性别'],index=['班级','姓名'])

df['总分']=df.英语+df.体育+df.军训+df.数分+df.高代+df.解几
bins = [min(df.总分)-1,400,450,max(df.总分)+1]   #将数据分成三段
labels=['400及其以下','400到450','450及其以上']  #给三段数据贴标签
总分分层 = pd.cut(df.总分,bins,labels=labels)
df['总分分层']= 总分分层
df.pivot_table(values=['总分'],
               index=['总分分层'],
               columns=['性别'],
               aggfunc=[numpy.size,numpy.mean])


#6.3.5  结构分析
import numpy as np
import pandas as pd
from pandas import read_excel
from pandas import pivot_table    #在spyder下也可以不导入
df = read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')
df['总分']=df.英语+df.体育+df.军训+df.数分+df.高代+df.解几
df_pt = df.pivot_table(values=['总分'],index=['班级'],columns=['性别'],aggfunc=[np.sum])
df_pt

df_pt.sum()
df_pt.sum(axis=1)  #按列合计
df_pt.div(df_pt.sum(axis=1),axis=0)  #按列占比
df_pt.div(df_pt.sum(axis=0),axis=1)  #按行占比


#6.3.6  相关分析
import numpy as np
import pandas as pd
from pandas import read_excel

df = read_excel(r'd:\yubg\出版资料\2021书稿\邮电出版社第2版——许金霞\第6章\i_nuc.xls',sheet_name='Sheet7')

df['高代'].corr(df['数分'])   #两列之间的相关度计算
df.loc[:,['英语','体育','军训','解几','数分','高代']].corr()
