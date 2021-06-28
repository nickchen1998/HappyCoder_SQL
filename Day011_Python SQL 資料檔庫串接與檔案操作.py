# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:05:37 2021

@author: nick
"""


# 一、問答申論題
# (一)、查詢 products 的 price 商品價格加總 (sum) 和分類 (category) 並使用 category 進行分組
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             port=3306,
                             db='demo_shop',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'SELECT category, SUM(price) FROM products GROUP BY category'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()
    
# (二)、使用 PyMySQL 和 for 迴圈新增 20 筆不同 名稱 的商品
try:
    with connection.cursor() as cursor:
        sql = 'INSERT INTO products (name, price, weight, category, created_at) VALUES (%s, %s, %s, %s, %s)'
        data = [(f'華速 intel i3 筆電_{index}', 20000, 2.12, 'NB', '2020-05-11 17:11:01') for index in range(1, 21)]
        cursor.executemany(sql, data)
    connection.commit()

    with connection.cursor() as cursor:
        sql = 'SELECT * FROM products'
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)        
finally:
    connection.close()
    
# 二、程式設計實作題
def even_num(number):
  if number % 2 ==0:
    with open('data.txt', 'w', encoding='utf8') as f:
      f.write("數字: {}\n偶數".format(number))
  else:
    with open('data.txt', 'w', encoding='utf8') as f:
      f.write("數字: {}\n非偶數".format(number))

num = int(input("請輸入一個整數: "))
even_num(num)

with open('data.txt', 'r', encoding='utf8') as f:
  print(f.read())