def sorted_squared(array):
    n = len(array)
    i,j = 0, n-1
    res = [0] * n
    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            res[k] = array[i] ** 2
            i += 1
        else:
            res[k] = array[j] ** 2
            j -= 1
    return res

arr = [-7, -3, 0, 1, 2, 3, 4]

print(sorted_squared(arr))