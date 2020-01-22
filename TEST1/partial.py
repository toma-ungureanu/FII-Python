def problema1(n):
    binar = bin(n)
    app = 0
    for item in binar:
        if item == "1":
            app += 1
    return app


def problema2(n):
    i = 1
    while i * i < n:
        i += 1
    return (i - 1) * (i - 1)


def palindrom(n):
    aux = n
    invers = 0
    while aux != 0:
        uc = aux % 10
        invers = invers * 10 + uc
        aux = aux // 10

    return n == invers


def problema3(my_list):
    pal = []
    for item in my_list:
        if palindrom(item):
            pal.append(item)
    return (len(pal), max(pal))


def problema4(my_list, letter):
    lista = []

    for item in my_list:
        if item[0] == letter:
            lista.append(item)
            break

    my_list.remove(lista[0])
    for i in range(1,len(my_list)):
        last_two = lista[i - 1][-2:]
        for item in my_list:
            first_two = item[:2]
            if last_two == first_two:
                lista.append(item)
                my_list.remove(item)
                break

    lista.append(my_list[0])
    return lista



def problema5(matrix):
    lista = []
    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] < matrix[i-1][j]:
                lista.append((i,j))


    return lista

