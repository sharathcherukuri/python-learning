def leaders(A,N):
    #Your code here
    
    '''
    Just return the list with leaders in it
    '''
    lead = []
    lead.append(A[N-1])
    print(lead)
    F_lead = A[N-1]
    
    for i in range(N-2,0,-1):
        if A[i] > F_lead:
            #print(A[i])
            lead.append(A[i])
            print(lead)
            F_lead = A[i]
   
    print(lead.reverse())
