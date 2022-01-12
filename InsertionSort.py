def main():
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(insertionSort(arr,n))

def insertionSort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    main()



