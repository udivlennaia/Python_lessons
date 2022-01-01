from functools import reduce


def mul_list(el_1, el_2):
    return el_1 * el_2


print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))
