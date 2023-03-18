def countingSort(niz, n):
    count={}

    for i in range(0,n):
        count[i] = 0

    for i in range(0,n):
        if niz[i] in count.keys():
            count[niz[i]] += 1
        else:
            count[niz[i]] = 1
    
    sortedArr = []
    i = 0
    while (n > 0):
        if (count[i] == 0) :
            i += 1
         
        else:
            sortedArr.append(i)
            count[i] -= 1
            n = n - 1
         
    return sortedArr
 
 
def printArr(niz, n):
    print("Sorted Array: ")
    for i in range(0,n):
        print(niz[i], " ")
 
niz1 = [ 6, 0, 7, 8, 7, 2, 0 ]
sortedArr1 = countingSort(niz1, len(niz1))
printArr(sortedArr1, len(sortedArr1))
 
niz2 = [ 4, 8, 1, 0, 1, 1, 0, 0 ]
sortedArr2 = countingSort(niz2, len(niz2))
printArr(sortedArr2, len(sortedArr2))