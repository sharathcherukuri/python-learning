def cycleSort(arr,n):
    for cs in range(0,n-1):
        item = arr[cs]
        pos = cs
        for i in range(cs+1,n):
            if arr[i] < item:
                pos += 1
        item ,arr[pos] = arr[pos],item
        print(arr)

        while cs!=pos:
            pos = cs
            for i in range(cs+1,n):
                if arr[i] < item :
                    pos += 1
            if item == arr[pos]:
                pos += 1
            item , arr[pos] = arr[pos],item
        print(arr)
    return arr
