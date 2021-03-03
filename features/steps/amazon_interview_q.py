# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

import timeit


def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    for l in string:
        if string.count(l) ==1:
            return l
    return ""
# O(n^2)


def unique_letter_optimal(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    d = {}
    for l in string:    # O(n)
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

    for k, v in d.items():  # O(n)
        if v == 1:
            return k

    return ""


# setup_code_1 = """"
# from __main__ import unique_letter
# string = 'askldhsakdsahdklhsahdsahhh skhdksahlhskhdslahd yyyyyyy shdphsjdsajdgjksgdkja'
# """
#
#
# setup_code_2 = """"
# from __main__ import unique_letter_optimal
# string = 'askldhsakdsahdklhsahdsahhh skhdksahlhskhdslahd yyyyyyy shdphsjdsajdgjksgdkja'
# """
#
#
# print(timeit.timeit(stmt="unique_letter(string)", setup = setup_code_1, number = 1000))
#
# print(timeit.timeit(stmt="unique_letter_optimal(string)", setup = setup_code_2, number = 1000))