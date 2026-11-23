import csv
import time
import random
from unittest.mock import MagicMock

random.seed(42)

# 模拟一台有噪声的万用表：基准12.345V，±0.02V噪声，偶尔跳一个异常值
def fake_measure():
    if random.random() < 0.1:          # 10%概率出现异常读数
        return f"+{random.uniform(11.5, 13.5):.4f}"
    return f"+{12.345 + random.uniform(-0.02, 0.02):.4f}"

inst = MagicMock()
inst.query.side_effect = lambda cmd: {
    "?IDN": "SIM,DMM,12345,1.0",
    "MEAS:VOLT:DC?": fake_measure(),
}.get(cmd, "ERROR")

print("仪器IDN:", inst.query("?IDN"))

rows = []
for i in range(20):                     # 采20个点，时间跨度更像真实采集
    value = inst.query("MEAS:VOLT:DC?")
    rows.append([time.strftime("%H:%M:%S"), value.strip()])
    time.sleep(0.3)

inst.close()

with open("voltage.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "voltage"])
    w.writerows(rows)

print("数据已保存到 voltage.csv")