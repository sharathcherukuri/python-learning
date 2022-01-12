from queue import Queue
def fivesixes(n):
    q = Queue()
    q.put("5")
    q.put("6")
    s = ""
    for i in range(n):
        s = q.get()
        print(q)
        print(s,end= " ")
        q.put(s+"5")
        q.put(s+"6")
    
    
