def main():
    n = int(input())
    low = 0 
    high = n-1
    arr = [int(x) for x in input().strip().split()]
    print(quickSort(arr,low,high))

def quickSort(arr,low,high):
    if low < high:
        i = partition(arr,low,high)

        quickSort(arr,low,i-1)
        quickSort(arr,i+1,high)
    return arr

def partition(arr,low,high):


    pivot = arr[high]

    i = low - 1

    for j in range(1,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j] , arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1 


if __name__ == "__main__":
    main()