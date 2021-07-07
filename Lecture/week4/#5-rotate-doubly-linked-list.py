# 5. Generate a function in clockwise rotation for each node (either char type or int type) in doubly linked list by N places, e.g. given 
#     list = None<-Head<=>c<=>i<=>v<=>i>=>c->None, from function call 
#     rotate_DLL(list, 3), the output will be like this 
#     None<-Head<=>v<=>i<=>c<=>c>=>i->None
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current
    
    def showContents(self):
        if(not self.head):
            return
        curr = self.head
        contents = []
        while curr:
            contents.append(curr.data)
            curr = curr.next
        print(contents)

    def rotate_DLL(list, n):
        if(not(list.head) or n < 1):
            print("Please provide valid linked list and n value ")
            return
        newList = []
        count = 1
        curr = list.head
        while count < n:
            newList.append(curr.data)
            curr = curr.next
            count += 1
        
        rotatedList = DoublyLinkedList()
        while curr:
            rotatedList.append(curr.data)
            curr = curr.next
        
        for node in newList:
            rotatedList.append(node)
        return rotatedList

dl = DoublyLinkedList()
dl.append('c')
dl.append('i')
dl.append('v')
dl.append('i')
dl.append('c')

dl.showContents()
rotated = dl.rotate_DLL(3)
rotated.showContents()
