# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:55:05 2021

@author: nick
"""


### 一、問答申論題
```
SELECT COUNT(amount), MAX(amount), SUM(amount), AVG(amount) FROM orders WHERE status = "CHECKED";

```

### 二、程式設實作做題
```
CREATE TABLE products(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  price INTEGER NOT NULL,
  category VARCHAR NOT NULL
);
CREATE TABLE orders(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  amount INTEGER NOT NULL,
  status VARCHAR NOT NULL,
  user_id INTEGER NOT NULL
);

INSERT INTO products(name, price, category) VALUES
  ("華速inteli3筆電", 20000, "NB"),
  ("Mac Pro筆電", 62000, "NB"),
  ("微星電競筆電", 32000, "NB"),
  ("戈林冰箱", 22000, "3C"),
  ("三力冰箱", 52000, "3C"),
  ("C 語言入門", 420, "Book"),
  ("python3 實戰", 580, "Book"),
  ("JavaScript 英雄", 1000, "Book"),
  ("Java 資料分析", 340, "NULL"),
  ("python 資料分析", 640, "NULL");


INSERT INTO orders(amount, status, user_id) VALUES
  (1000, "REFUND", 2),
  (12000, "CHECKED", 1),
  (2350, "CHECKED", 3),
  (1720, "CHECKED", 4),
  (500, "CHECKED", 5),
  (7600, "PENDING", 6);

SELECT name FROM products WHERE price > (SELECT AVG(amount) FROM orders);
```