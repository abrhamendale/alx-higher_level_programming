#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        j = 0
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            j = j + 1
    except IndexError:
        print('', end='')
    print()
    return j
