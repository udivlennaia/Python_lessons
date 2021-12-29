def my_func(num_1: int, num_2: int, num_3: int) -> int:
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only a numbers'
