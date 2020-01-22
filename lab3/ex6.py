def unique_duplicate(list1):
    duplicates = set([x for x in list1 if list1.count(x) > 1])
    uniques = set([x for x in list1 if list1.count(x) == 1])

    return tuple((len(duplicates), len(uniques)))


def main():
    set1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 1, 2, 3, 4, 1]
    print(set1)
    print(unique_duplicate(set1))


main()
