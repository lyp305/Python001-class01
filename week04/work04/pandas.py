import pymysql
import pandas as pd

sql = 'SELECT *  FROM data'
sql1 = 'SELECT *  FROM table1'
sql2 = 'SELECT *  FROM table2'

conn = pymysql.connect('ip', 'name', 'pass', 'dbname', 'charset=utf8')
df = pd.read_sql(sql, conn)
df1 = pd.read_sql(sql1, conn)
df2 = pd.read_sql(sql2, conn)

# 1. SELECT * FROM data;
df[0:]

# 2. SELECT * FROM data LIMIT 10;

df[0:10]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']

# 4.SELECT COUNT(id) FROM data;

df['id'].count()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[(df['id'] < 1000) & (df['age'] > 30)]

# 6.SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

df.drop_duplicates(subset=['order_id', 'id']).groupby('id').aggregate({'order_id': 'count', 'id': 'max'})

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

pd.merge(df1, df2, left_on='id', right_on='id')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;

pd.merge(df1, df2, how='outer')

# 9. DELETE FROM table1 WHERE id=10;

df1[df1['id'] != '10']

# 10.ALTER TABLE table1 DROP COLUMN column_name;
colname = 'order_id'
df.drop(colname ,axis = 1)