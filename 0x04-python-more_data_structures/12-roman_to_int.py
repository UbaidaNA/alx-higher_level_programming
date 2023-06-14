#!/usr/bin/python3
def subtract(list_numeral):
    sub = 0
    max_list = max(list_numeral)

    for n in list_numeral:
        if max_list > n:
            sub += n

    return (max_list - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return (0)

    if not isinstance(roman_string, str):
        return (0)

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_numerals.keys())

    numeral = 0
    last_roman = 0
    list_numeral = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if roman_numerals.get(ch) <= last_roman:
                    numeral += subtract(list_numeral)
                    list_numeral = [roman_numerals.get(ch)]
                else:
                    list_numeral.append(roman_numerals.get(ch))

                last_roman = roman_numerals.get(ch)

    numeral += subtract(list_numeral)

    return (numeral)    
