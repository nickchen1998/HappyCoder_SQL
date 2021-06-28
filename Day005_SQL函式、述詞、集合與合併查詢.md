# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:55:56 2021

@author: nick
"""


### 一、問答申論題
```
SELECT SUBSTR(price*0.9, 1, 3) FROM products;

SELECT COALESCE(category, '未分類') FROM products;
```

### 二、程式設計實作題
```
CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  email VARCHAR NOT NULL,
  age INTEGER NOT NULL
);
CREATE TABLE orders(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  amount INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  created_at VARCHAR NOT NULL
);

INSERT INTO users(name, email, age) VALUES
('Jack Hung', 'jackh32@gmail.com', 20),
('Tony Liu', 'tonykk@gmail.com', 62),
('Amy Chang', 'amychang@gmail.com', 32),
('Kay Wang', 'kkk@gmail.com', 28);

INSERT INTO orders(amount, customer_id, created_at) VALUES
(2900, 1, (SELECT CURRENT_TIMESTAMP)),
(1400, 3, (SELECT CURRENT_TIMESTAMP)),
(870, 2, (SELECT CURRENT_TIMESTAMP));

SELECT * FROM users INNER JOIN orders ON users.id = orders.customer_id ORDER BY age DESC;

SELECT * FROM users LEFT OUTER JOIN orders ON users.id = orders.customer_id ORDER BY age DESC;
```