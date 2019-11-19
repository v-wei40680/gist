"""
pandas insert to mysql
"""

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
