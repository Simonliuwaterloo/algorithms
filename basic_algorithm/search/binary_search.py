def binary_search(target, data_input):
    data = data_input
    length = len(data)
    ref = int(length/2)
    while data[ref] != target:
        if target < data[ref]:
            ref = int(ref/2)
        else:
            ref = int((ref + length)/2)


    print(ref)
