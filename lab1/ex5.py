def spiralPrint(m, n, a):
    k = 0
    l = 0

    while k < m and l < n:

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k * m + i], end=" ")

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i * m + n - 1], end=" ")

        n -= 1

        # Print the last row from
        # the remaining rows
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                print(a[(m - 1) * m + i], end=" ")

            m -= 1

        # Print the first column from
        # the remaining columns
        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i * m + l], end=" ")
            l += 1


def main():
    rows = int(input("Enter the number of rows:"))
    columns = int(input("Enter the number of columns:"))
    matrix = ""
    for i in range(rows):
        a = ""
        for j in range(columns):
            a += input("Enter matrix[" + str(i) + "][" + str(j) + "]: ")
        matrix += a

    for i in range(rows):
        for j in range(columns):
            print(matrix[i * rows + j], end=" ")
        print()

    print()
    spiralPrint(rows, columns, matrix)


main()
