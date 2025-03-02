def monotonic(arr):
    if len(arr) <=1:
        return True 

    increasing = decreasing = True 

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            increasing = False 
        if arr[i] < arr[i+1]:
            decreasing = False 

    return increasing or decreasing     


    
arr1 = [1, 2, 3, 4]      # Monotonic increasing → True
arr2 = [9, 7, 5, 3]      # Monotonic decreasing → True
arr3 = [3, 4, 5, 9, 7]   # Not monotonic → False
arr4 = [5, 5, 5, 5]      # All elements equal → True ✅
arr5 = []                # Empty array → True ✅

print(monotonic(arr1))  # ✅ True
print(monotonic(arr2))  # ✅ True
print(monotonic(arr2))  # ✅ True
print(monotonic(arr3))  # ❌ False
print(monotonic(arr4))  # ✅ True
print(monotonic(arr5))  # ✅ True


