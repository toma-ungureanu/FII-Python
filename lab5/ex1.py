def operations(a, b):
    print(a-b)
    print(a+b)
    print(a/b)
    print(a*b)


def main():
    try:
        a = input(" Enter an integer: ")
        b = input(" Enter the second integer: ")

        if not int(a) or not int(b):
            raise ValueError

        operations(int(a), int(b))
    except ValueError:
        print(" Enter 2 numbers!")


main()
