arr = [1, 2, 3, 4, 5]

def pair(array) :
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])


pair(arr)