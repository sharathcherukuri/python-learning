def reverseInGroups(A,N,K):
    #Your code here
    i =0
    for i in range(0,N,i+K):
        left = i
        right = i+K-1
        if right >= N:
            right = N-1
        while left < right :
            A[left], A[right]= A[right], A[left]
            left += 1
            right -= 1
    print(A)
