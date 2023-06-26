#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    try:
        for n in range(list_length):
            try:
                element_1 = my_list_1[n]
                element_2 = my_list_2[n]
                if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                    if element_2 == 0:
                        res_list.append(0)
                        print("division by 0")
                    else:
                        res = element_1 / element_2
                        res_list.append(res)
                else:
                    res_list.append(0)
                    print("wrong_type")
            except IndexError:
                print("out of range")
                res_list.append(0)
    finally:
        return res_list
