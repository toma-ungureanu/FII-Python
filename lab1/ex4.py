def upper_camel_2_lower_case(string):
    string = string.replace(string[0], string[0].lower(), 1)
    for i in range(1, len(string)):
        if string[i].isupper():
            string = string.replace(string[i], string[i].lower(), 1)
            string = string[:i] + "_" + string[i:]

    # for i in range(int(len(string)/2), len(string)):
    #     if string[i].isupper():
    #         string = string.replace(string[i], string[i].lower(), 1)
    #         string = string[:i] + "_" + string[i:]
    return string


def main():
    string1 = input("Enter a string with UpperCamelCase: ")
    print(upper_camel_2_lower_case(string1))


main()
