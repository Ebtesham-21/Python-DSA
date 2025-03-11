array1= [1, 2, 3, 4]
array2 = [1, 2, 3, 5]
def commonItemMatch(arr1, arr2):
    for i in range (len(arr1)):
        for j in range (len(arr2)):
           
           if (arr1[i] == arr2[j]):
               print(True)
    return False    

commonItemMatch(array1, array2)
           
           
           
                   

        