# 3.   PriorityQueue is a queue with following propertiesa.   
#  Every item has a priority associated with it.b.  
#  In pop operation, an element with high priority will be dequeued (deleted) before an element with low priority.c.  
# If two elements have the same priority, they are served according to their order in the queue.For example, 
# each element in a given queue is char type and priority of each element is ASCII code value, write functions to complete push and pop operations 


from queue import Queue 

class PriorityQue:
    def __init__(self):
        self.items = Queue()
    
    def push(self, data):
        self.items.put(data)

    def size(self):
        return self.items.qsize()
    
    def pop(self):
        #check for priority and pop 
        priorityIndex = 0
        for i in range(0, self.size()):
            if self.items.queue[priorityIndex] < self.items.queue[i]:
                priorityIndex = i
        itemRemoved = self.items.queue[priorityIndex]
        del self.items.queue[priorityIndex]
        return self.items.queue[priorityIndex]



pq1 = PriorityQue()

pq1.push('C')
pq1.push('O')
pq1.push('D')
pq1.push('A')

print(pq1.items.queue, pq1.size())
print("Removes", pq1.pop())
print("After removal", pq1.items.queue, pq1.size())
pq1.push('B')
print(pq1.pop())
print(pq1.items.queue, pq1.size())



