# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:03:08 2021

@author: nick
"""


# 一、問答申論題
x = int(input('請輸入一個整數: '))
sum = 0

for i in range(x+1):
    sum += i

print("使用 for 進行連加: {}".format(sum))

sum_2 = 0
i = 0
while i != x:
    i += 1
    sum_2 += i

print('使用 while 進行連加: {}'.format(sum_2))

# 二、程式設計實作題
def get_is_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

def get_is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

x = int(input('請輸入一個整數: '))

print("判斷此數是否為奇數: {}".format(get_is_odd(x)))
print("判斷此數是否為質數: {}".format(get_is_prime_number(x)))
