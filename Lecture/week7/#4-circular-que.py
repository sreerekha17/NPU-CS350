# 4.   Given a circular queue with max size = M to save each element, after several times enqueue (insert) & dequeue(delete) operations,
# front & rear have their own values, write a function/method getNumElem(size, front, rear)to find how many elements are in the circular queue 

class CircularQueue:

    #Constructor
    def __init__(self, maxSize):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = maxSize

    #Adding elements to the queue
    def enqueue(self,data):
        if getNumElem(self.maxSize, self.head, self.tail) == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    #Removing elements from the queue
    def dequeue(self):
        if getNumElem(self.maxSize, self.head, self.tail)==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

def getNumElem(size, front, rear):
    if rear >= front:
        return rear - front
    return size - (front - rear)

cl1 = CircularQueue(10)
cl1.enqueue(10)
cl1.enqueue(20)
cl1.enqueue(30)
cl1.enqueue(40)
cl1.enqueue(50)

print("Size of queue after adding 5 items", getNumElem(10, cl1.head, cl1.tail))
print(cl1.dequeue()) #removed first entry

print("Size after removing 1 entry is", getNumElem(10, cl1.head, cl1.tail))
