def operations(list1, list2):
    final_set = set()
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    subtraction_set1 = set1.difference(set2)
    subtraction_set2 = set2.difference(set1)
    reunion_set = set1.union(set2)

    final_set.add(frozenset(intersection))
    final_set.add(frozenset(subtraction_set2))
    final_set.add(frozenset(subtraction_set1))
    final_set.add(frozenset(reunion_set))
    return final_set


def main():
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    b = {5, 6, 7, 8, 9, 10, 11, 12}
    print(operations(a, b))

    c = {"Ana", "are", "mere", "."}
    d = {"Irina", "mananca", "mere", "."}
    print(operations(c, d))


main()
