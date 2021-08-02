# Given a queue with a series of int type elements as follows, 
# write a program to reverse the sequence by a new queue WITHOUT using other data structures, 
# like temporary array or list


# Solution by using a circular queue
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

    def reverseQueue(self):
        tail = self.tail
        self.tail = self.head
        self.head = tail
        print("head, tail", self.head, self.tail)

    def peekQueue(self):
        step = 1
        if self.head > self.tail:
            step = -1
            for i in range(self.head-1, self.tail, step):
                print(self.queue[i])

        else:
            for i in range(self.head, self.tail, step):
                print(self.queue[i])

def getNumElem(size, front, rear):
    if rear >= front:
        return rear - front
    return size - (front - rear)

q1 = CircularQueue(12)

q1.enqueue(11)
q1.enqueue(9)
q1.enqueue(8)
q1.enqueue(12)
q1.enqueue(4)
q1.enqueue(13)
q1.enqueue(16)
q1.enqueue(7)

print("Original queue")
q1.peekQueue()

q1.reverseQueue()
print("Queue after reverse")

q1.peekQueue()


