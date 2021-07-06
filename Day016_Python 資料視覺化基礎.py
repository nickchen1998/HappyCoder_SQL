# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:46:29 2021

@author: nick
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./110年4月份人口數統計表.csv', encoding='big5')



data = df.loc[:5, ['村別數', '鄰數', '男數', '女數']]


data = data.set_index('村別數')


data.plot(kind='bar')

plt.show()