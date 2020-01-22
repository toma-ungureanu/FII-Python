def count_appearances(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1.startswith(string2, i):
            count += 1
    return count


def main():
    string1 = input("Enter a string to search in: ")
    string2 = input("Enter a string to search for in the first: ")
    print(count_appearances(string1, string2))
    return 0


main()
