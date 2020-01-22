class Error(Exception):
    """Exception"""
    pass


class NegativeValueError(Error):
    """Raised when the input value is negative"""
    pass


class FloatError(Error):
    """Raised when the input value is negative"""
    pass


def find_gcd_2numbers(num1, num2):
    try:
        if num1 < 0 or num2 < 0:
            raise NegativeValueError
        if isinstance(num1, float) or isinstance(num2, float):
            raise FloatError
        while num2:
            num1, num2 = num2, num1 % num2
        return num1
    except (NegativeValueError, FloatError):
        print("You didn't enter a positive integer")


def main():
    numbers = []
    while True:
        try:
            num = int(input("Enter an integer: "))
            numbers.append(num)
        except ValueError:
            break

    if len(numbers) < 2:
        print("Please enter more values")
        return 1
    print(numbers)
    main_num1 = numbers[0]
    main_num2 = numbers[1]

    gcd = find_gcd_2numbers(main_num1, main_num2)
    for i in range(2, len(numbers)):
        gcd = find_gcd_2numbers(gcd, numbers[i])
    print(gcd)
    return 0


main()
