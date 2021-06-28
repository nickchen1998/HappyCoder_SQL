# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:59:47 2021

@author: nick
"""


### 一、問答申論題
透過統計顧客將商品加入購物車的次數和最近一次的消費時間以及相差天數做評分，來評估哪些顧客需要我們推一把使其能進行商品的結帳。
```
CREATE VIEW RFM 
AS
    SELECT
        user_id,
        /* 最近一次消費時間 */
        MAX(create_at) AS recency_dt,
        /* 最近購買日期和目前相差天數 */
        DATEDIFF('2020-07-30', DATE(MAX(create_at))) AS recency,
        /* 統計消費總次數 */
        SUM(CASE WHEN action_type = 'ADD_CART' THEN 1 ELSE 0 END) AS frequency,
        /* 統計消費總金額 */
        SUM(purchase_amount) AS monetary
    FROM user_action_logs
    GROUP BY user_id
```

### 二、程式設計實作題
```
CREATE VIEW RFM_points
AS
    SELECT
        user_id,
        recency,
        monetary,
        frequency,
        CASE
            WHEN recency < 7 THEN 5
            WHEN recency < 14 THEN 4
            WHEN recency < 30 THEN 3
            WHEN recency < 60 THEN 2
            ELSE 1
        END AS recency_point,
        CASE
            WHEN ADD_CART > 10 THEN 5
            WHEN ADD_CART > 5 THEN 4
            WHEN ADD_CART > 3 THEN 3
            WHEN ADD_CART > 2 THEN 2
            ELSE 1
        END AS frequency_point,
        CASE
            WHEN monetary > 100000 THEN 5
            WHEN monetary > 10000 THEN 4
            WHEN monetary > 1000 THEN 3
            WHEN monetary > 500 THEN 2
            ELSE 1
        END AS monetary_point
    FROM RFM;
```
```
SELECT user_id, recency_point, frequency_point, monetary_point, (recency_point + frequency_point + monetary_point) 
AS RFM_points FROM RFM_points ORDER BY RFM_points DESC

```