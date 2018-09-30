#!/usr/bin/env python
import pandas as pd
import numpy as np

def insertion_sort(data_name):
    raw_data = list()
    for n in range (0,len(list(pd.read_csv(data_name)))):
        raw_data.append(int(list(pd.read_csv(data_name))[n]))
    number_of_element = len(raw_data)

    for m in range (0, len(raw_data)):
        insertion = raw_data[m]
        left_number = 0
        for l in range (m -1, -1, -1):
            if raw_data[m] < raw_data[l]:
                left_number = raw_data[l]

        if left_number != 0:
            index_of_left = raw_data.index(left_number)
            raw_data.insert(index_of_left, raw_data[m])
            del raw_data[m + 1]

    return("\n", raw_data)
