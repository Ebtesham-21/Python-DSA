arr = [1, 2, 3, 4]

def sorted_squared(array):
    n = len(array)
    res = [0] * n
    for i in range(n):
        res[i] = array[i] ** 2
    res.sort()
    return res


print(sorted_squared(arr))