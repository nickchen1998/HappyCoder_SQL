# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:58:08 2021

@author: nick
"""


### 一、問答申論題
```
SELECT orders.id, products.category, AVG(products.price) 
FROM orders 
INNER JOIN order_details ON order_details.order_id = orders.id 
INNER JOIN products ON order_details.product_id = products.id 
GROUP BY orders.id, products.category;
```

### 二、程式設計實作題
```
SELECT id, amount, DATE(created_at), AVG(amount) 
OVER (ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg_price 
FROM orders 
GROUP BY DATE(created_at) 
ORDER BY DATE(created_at);
```