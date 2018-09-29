#!/usr/bin/env python
import pandas as pd
import numpy as np


raw_data = list()
for n in range(0,len(list(pd.read_csv('data.txt')))):
    raw_data.append(int(list(pd.read_csv('data.txt'))[n]))
print(raw_data)


count = 0
while count < len(raw_data) + 1:
    for n in range(1, len(raw_data)):
        if raw_data[-n] < raw_data[-n - 1]:
            tmp = raw_data[-n]
            raw_data[-n] = raw_data[-n - 1]
            raw_data[-n - 1] = tmp
    count = count + 1
print(raw_data)
