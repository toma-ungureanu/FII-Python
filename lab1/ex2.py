vowels = "aeiouAEIOU"


class Error(Exception):
    """Exception"""
    pass


class StringError(Error):
    """Raised when the input value is negative"""
    pass


def check_vowels(string1):
    try:
        count = 0
        global vowels
        if not isinstance(string1, str):
            raise StringError
        for char in string1:
            for vowel in vowels:
                if char == vowel:
                    count += 1
        return count
    except StringError:
        print("Enter a string")


def main():
    string = input("Enter a string: ")
    print(check_vowels(string))
    return 0


main()
