# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:35:41 2021

@author: nick
"""
import numpy as np

a = np.arange(1, 26).reshape(5, 5)
print(a)
print()

product = np.array([[320, 470, 190], [1.5, 10, 6]])

order = np.array([[2, 3, 3], [1, 4, 2], [0, 1, 1]])

print(product.dot(order))


# 補充: dot 為正常的矩陣相乘 直的*橫的
# 補充: inner 為(1)1 (1)2 (1)3......