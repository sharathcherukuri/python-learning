class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head

        while temp:
            print(temp.data,"->",end="")
            temp = temp.next
    def insert(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
            

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
if  __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second

    second.next = third

    third.next = None
    llist.insert(10)
    llist.insert(20)
    llist.printList()
    
        
