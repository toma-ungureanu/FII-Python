def prime1(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(2, n ** 0.5 + 1):
        if n % d == 0:
            return False
    return True

prime1(101)