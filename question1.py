arr = [-4, -2, 0, 1, 2, 3]

def square_elements(arr):
    squared_arr = []

    for i in range(len(arr)):
        for j in range(1):
            squared_arr.append(arr[i] ** 2)

    return sorted(squared_arr)  

square_result = square_elements(arr)
print(square_result)


