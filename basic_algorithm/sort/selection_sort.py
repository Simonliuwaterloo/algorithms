#!/usr/bin/env python
import pandas as pd
import numpy as np

def selection_sort(data_name):
    raw_data = list()
    for n in range(0,len(list(pd.read_csv(data_name)))):
        raw_data.append(int(list(pd.read_csv(data_name))[n]))

    for m in range(0, len(raw_data)):
        a = raw_data[m]
        for n in range(m, len(raw_data)):
            if raw_data[n] < a:
                a = raw_data[n]

        i = raw_data[m]

        c = raw_data.index(a)

        raw_data[m] = a
        raw_data[c] = i
    return(raw_data)
