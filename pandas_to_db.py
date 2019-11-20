"""
pandas insert to mysql
"""
import json

import pandas as pd
import pymysql  
from sqlalchemy import create_engine

df = pd.read_excel("C://Users/Administrator/Desktop/o.xlsx", dtype={'_id': str, 'quantity': int, 'sellerFlag': int})
print(df.dtypes)
df = df.rename(columns={'_id': 'id'})

engine = create_engine('mysql+pymysql://user:password@localhost:3306/database')

# 将新建的DataFrame储存为MySQL中的数据表，不储存index列
df.to_sql('tmall_trades', engine, index= False, if_exists='append')

print("Write to MySQL successfully!")

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='goods')

def to_mysql():
  """
  second way pandas Dataframe to mysql.
  """
  df_datas = df.to_json(orient='records')
  datas= json.loads(df_datas)
  table = 'items'
  keys = datas[0].keys()
  keys = ', '.join(keys)
  cursor = db.cursor()
  
  for data in datas:
      values = ', '.join(['% s'] * len(data))
      sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
      try:
         if cursor.execute(sql, tuple(data.values())):
             print('Successful')
             db.commit()
      except:
          print('Failed')
          db.rollback()
  db.close()
  cursor.close()
  
