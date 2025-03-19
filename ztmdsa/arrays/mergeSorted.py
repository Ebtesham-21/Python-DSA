while(array1Item || array2Item){
    if (array1Item < array2Item){
        mergedArray.push(array1Item)
        array1Item = array1[i];
        i++;
    }
}