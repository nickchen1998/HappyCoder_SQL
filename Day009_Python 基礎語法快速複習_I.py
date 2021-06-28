# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:02:02 2021

@author: nick
"""


# 一、問答申論題
x = ''
x += input()
result = x.split(',')
print(result[len(result)-1])

# 二、程式設計實作題
height = eval(input('請輸入身高: '))
weight = eval(input('請輸入體重: '))

bmi = weight/((height/100)**2)
print()
print("您的身高為: {}公分\n您的體重為: {}公斤\n您的BMI為: {:.2f}".format(height, weight, bmi))