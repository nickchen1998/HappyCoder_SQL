# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:11:30 2021

@author: nick
"""


import pandas


datas = pandas.read_csv('11005.csv')

count = datas.value_counts('設立核准日期')
print(count)

date_group = datas.groupby(['設立核准日期'])
print(date_group.get_group(1100505))