def getDictionary(arg):
    dictionary = {}
    for a in arg:
        if a in dictionary:
            dictionary[a] += 1
        else:
            dictionary[a] = 1

    return dictionary


def list_difference(list1, list2):
    subtraction_list1 = list([item for item in list1 if item not in list2])
    return subtraction_list1


def compare_dictionaries(dict1, dict2):

    for key in dict1:
        if isinstance(dict1[key], dict):
            compare_dictionaries(dict1, dict2)


def main():
    string1 = "Anna has apples"
    string2 = "Mary had a little lamb"
    string3 = "Jane Doe is a common name"
    string4 = "John Doe is not a real name"

    dictionary1 = getDictionary(string1)
    dictionary2 = getDictionary(string2)

    dictionary_list = {}
    dictionary_list1 = {}
    dictionary_list['dict1'] = getDictionary(string1)
    dictionary_list['dict2'] = getDictionary(string1)
    dictionary_list1['dict3'] = getDictionary(string3)
    dictionary_list1['dict4'] = getDictionary(string4)
    dictionary_list['multeDict'] = dictionary_list1
    # print(dictionary_list)
    compare_dictionaries(dictionary_list, dictionary1)


main()
