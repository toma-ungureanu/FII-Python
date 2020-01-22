def problem1(my_list):
    even_ints = (filter(lambda x: x % 2 == 0, my_list))
    odd_ints = (filter(lambda x: x % 2 != 0, my_list))
    zipped = zip(even_ints, odd_ints)
    return [x for x in zipped]


def problem2(pairs):
    dict_list = []
    for item in pairs:
        dictionar = {'sum': item[0] + item[1], 'prod': item[0] * item[1], 'pow': item[0] ** item[1]}
        dict_list.append(dictionar)
    return dict_list
