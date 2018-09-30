#!/usr/bin/env python
import pandas as pd
import numpy as np

def bubble_sort(data_name):
    raw_data = list()
    for n in range(0,len(list(pd.read_csv(data_name)))):
        raw_data.append(int(list(pd.read_csv(data_name))[n]))



    count = 0
    while count < len(raw_data) + 1:
        for n in range(1, len(raw_data)):
            if raw_data[-n] < raw_data[-n - 1]:
                tmp = raw_data[-n]
                raw_data[-n] = raw_data[-n - 1]
                raw_data[-n - 1] = tmp
        count = count + 1
    return(raw_data)
