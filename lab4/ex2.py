def checker(name_list, name):
    mij = len(name_list) // 2
    if name == name_list[mij][1]:
        return True
    if len(name_list) < 2:
        return False
    if name < name_list[mij][1]:
        return checker(name_list[:mij], name)
    else:
        return checker(name_list[mij:], name)


def main():
    name = "Miron"
    name_tuple = ("Andrei", "Miron")
    name_tuple1 = ("Toma", "Mironel")
    name_list = [name_tuple, name_tuple1]
    print(checker(name_list, name))


main()

