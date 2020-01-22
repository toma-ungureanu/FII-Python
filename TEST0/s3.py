def problema1(n):
    s = 0
    for i in range(0, n + 1):
        s += i
    return s


def problema5(n):
    integer = int(n, 8)
    temp = integer
    inv = 0
    uc = 0
    while temp != 0:
        uc = temp % 10
        inv = inv * 10 + uc
        temp = temp // 10
    if inv == integer:
        return True
    return False

print(problema5("10"))
