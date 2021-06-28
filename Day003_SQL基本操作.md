# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:51:29 2021

@author: nick
"""


### 一、問答申論題
```
SELECT * FROM users WHERE age > 20 and gender = 'Male'
```

### 二、程式設計實做題
程式碼說明:
於 SQLite 資料庫中，AUTOINCREMENT 代表此欄位會自動產生升冪的序列 ID
由於在創建資料表時已指定此欄位自動產生
因此於下方進行資料插入時，只需選定後兩個欄位進行資料的插入
```
CREATE TABLE products(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  price INTEGER NOT NULL
);

INSERT INTO products(name, price) VALUES(
  "ASUS 手機", 2000
);
INSERT INTO products(name, price) VALUES(
  "iPhone10", 16000
);
INSERT INTO products(name, price) VALUES(
   "ACER 手機", 3000
);

SELECT * FROM products;
```