arr = [1, 3, 5, 4]
def isSorted(arr):
    l = len(arr)

    if l == 0 or l == 1:
        return True
    
    if arr[0] > arr[1]:
        return False 
    
    return isSorted(arr[1:])


print(isSorted(arr))