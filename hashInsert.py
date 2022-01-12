def hashf(key,hashSize):
    return key%hashSize
def separateChaining( hashSize, arr, sizeOfArray):
    #Your code here
    #return hashtable
    li = [[] for x in range(hashSize)]
    for i in range(len(arr)):
        index = hashf(arr[i],hashSize)
        li[index] = arr[i]
    return li
