#!/usr/bin/python3
def max_integer(my_list=[]):
    span = len(my_list)

    if span == 0:
        return (NOne)

    max_num = my_list[0]

    for i in range(1, span):
        if my_list[i] > max_num:
            max_num = my_list[i]
            
    return (max_num)
