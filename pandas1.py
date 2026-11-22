import pandas as pd

import numpy as np

df = pd.read_csv('wafer_yield.csv', sep=',', header=0)
print(df['wafer_id'][0])

# 过滤出所有 yield_rate 小于 threshold 的行

no_pass = df[df['yield_rate'] < df['threshold']]
print(no_pass)

# df.groupby('wafer_id')
g2 = df.groupby('test_date')['yield_rate'].mean()

print(g2)