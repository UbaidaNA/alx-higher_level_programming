#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for n in range(x):
            if isinstance(my_list[n], int):
                print("{:d}".format(my_list[n]), end="")
                i += 1
    except IndexError:
        pass
    finally:
        print()
        return i
