import pandas as pd

df = pd.read_csv('voltage.csv')

df['voltage'] = df['voltage'].astype(float)

print(df['voltage'].describe())

# 找出超出规格的点
lower, upper = 12.345 - 0.05, 12.345 + 0.05

outliers = df[(df['voltage'] < lower) | (df['voltage'] > upper)]

print(f"超出规格的点有 {len(outliers)} 个")
print(outliers)

# 判定：如果超出规格的点超过10%,判定FAIL
fail_rate = len(outliers) / len(df)

print(f"超出规格的点占比为 {fail_rate:.2%}")

print("判定结果:", "PASS" if fail_rate <= 0.1 else "FAIL")
