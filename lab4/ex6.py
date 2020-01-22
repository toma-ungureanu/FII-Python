dictionary = {
    'a': 1,
    'b':
        {
            'c': 3,
            'd':
                {
                    'e': 5,
                    'f': 6
                }
        }
}


def recurse(dicti, sep, sep1=""):
    for key in dicti:
        if isinstance(dicti[key], dict):
            recurse(dicti[key], sep, f"{sep1}{key}{sep}")
        else:
            print(f"{sep1}{key}{sep}{dicti[key]}")

recurse(dictionary, "-")
