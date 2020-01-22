def getDictionary(arg):
    dictionary = {}
    for a in arg:
        dictionary[a] = dictionary.get(a, 0) + 1
    return dictionary


def main():
    string = "Anna has apples"
    print(getDictionary(string))


main()
