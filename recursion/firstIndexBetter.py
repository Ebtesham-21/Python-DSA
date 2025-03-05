def firstIndexB(a, x, si):
    l = len(a)
    if si == l:
        return -1
    
    if a[si] == x:
        return si
    
    smallerListOutput = firstIndexB(a, x, si+1)
    return smallerListOutput