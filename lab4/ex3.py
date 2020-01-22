dictionary = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
    "//": lambda a, b: a % b
}


def apply_operator(operator, a, b):
    print(dictionary.get(operator)(a, b))


def main():
    a = 4
    b = 7
    apply_operator("//", a, b)


main()
