dictionary = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_operator(operator, *a, **b):
    print(dictionary[operator](a, b))


def main():
    operator = "print_only_args"
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = ["alb", "rosu", "verde"]
    c = ["x", "y", "z"]
    apply_operator(operator, *a, b,c)


main()
