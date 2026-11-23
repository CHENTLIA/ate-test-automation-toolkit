import pyvisa

import csv

import time

import os

print(os.getcwd())

rm = pyvisa.ResourceManager(r'F:\shopifyJob\newDay1\my_sim.yaml@sim')

print('可用资源', rm.list_resources())

inst = rm.open_resource('ASRL1::INSTR', read_termination='\n')


print('仪器IDN', inst.query('?IDN'))

rows = []

for i in range(5):
    value = inst.query('MEAS:VOLT:DC?')

    rows.append([time.strftime("%H:%M:%S"), value.strip()])
    time.sleep(0.2)

inst.close()

with open('voltage.csv', 'w', newline='') as f:
    w = csv.writer(f)

    w.writerow(['timestamp', 'voltage'])

    w.writerows(rows)

print('数据已保存到 voltage.csv')