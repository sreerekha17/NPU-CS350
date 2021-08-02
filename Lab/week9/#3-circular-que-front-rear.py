# In a circular queue with size = 6, write a program to find the final locations of front & rear after the following operations. 

# a. d, e, b, g, h	- enqueue (insert) operation
# b. d, e		- dequeue (delete) operation
# c. i , j , k , l , m	- enqueue (insert) operation
# d. b		- dequeue (delete) operation
# e. n, o, p, q, r	- enqueue (insert) operation


class CircularQueue:
    def __init__(self, maxSize):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = maxSize

    def enqueue(self,data):
        if getNumElem(self.maxSize, self.head, self.tail) == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    def dequeue(self):
        if getNumElem(self.maxSize, self.head, self.tail)==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

def findFrontAndRear(q):
    print("head is at", q.head, "and tail is at", q.tail)
    print("Data at head is", q.queue[q.head], "and data at tail is", q.queue[q.tail])


def getNumElem(size, front, rear):
    if rear >= front:
        return rear - front
    return size - (front - rear)



cl1 = CircularQueue(6)
cl1.enqueue('d')
cl1.enqueue('e')
cl1.enqueue('b')
cl1.enqueue('g')
cl1.enqueue('h')

print(cl1.dequeue())
print(cl1.dequeue())

cl1.enqueue('i')
cl1.enqueue('j')
cl1.enqueue('k')
cl1.enqueue('l')
cl1.enqueue('m')

print(cl1.dequeue())

cl1.enqueue('n')
cl1.enqueue('o')
cl1.enqueue('p')
cl1.enqueue('q')
cl1.enqueue('r')

findFrontAndRear(cl1)