#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    result_1 = 0
    result_2 = 0
    for i, j in my_list:
        result_1 += i * j
        result_2 += j
    return (result_1 / result_2)
