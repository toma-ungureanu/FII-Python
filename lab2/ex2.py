def function(x, *y):
    concat = sum(y, [])
    result = list()
    for item in concat:
        if concat.count(item) == x:
            if item not in result:
                result.append(item)

    return result


function(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
