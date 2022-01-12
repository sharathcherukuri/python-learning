class LinkedList():
    def __init__(self):
        self.head = None
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insertEnd(head,x):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    temp.next = None
    return head

    return head
def printList(head):
    while head != None:
        print(head.data,end =" ")
        head = head.next

if __name__ == "__main__":
    lk = LinkedList()
    insertEnd(lk.head,10)
    insertEnd(lk.head,20)
    insertEnd(lk.head,30)
    insertEnd(lk.head,40)
    printList(lk.head)
