class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def push(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    def insertAfter(self,prev,data):
        if prev == None:
            print("prev should be in the LInkedList")
        temp = Node(data)
        temp.next = prev.next
        prev.next = temp

    def append(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = temp
        temp.next = None
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data,end=" ")
            curr= curr.next
if __name__=="__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.printList()
    print()
    llist.insertAfter(llist.head,30)
    llist.append(40)
    llist.printList()



