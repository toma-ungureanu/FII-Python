import operator


def sortNames(name_list):
    return sorted(name_list, key=operator.itemgetter(1))


def main():
    name1 = ("Toma", "Ungureanu")
    name2 = ("Florin", "Iavorschi")
    name3 = ("Florinel", "Coman")
    name_list = [name1, name2, name3]
    print(sortNames(name_list))


main()
