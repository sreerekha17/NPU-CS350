# Assuming that there is a queue with int type elements, 
# like q = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 
# and given unsigned int number n = 5 for example, 
# create a function rev(q, n) to reverse elements from first to  elements in a queue, 
# such as {5, 4, 3, 2, 1, 6, 7, 8, 9, 10}

from queue import Queue


def reverse(q, n):
    if not q.qsize() or q.qsize() < n or n < 1:
        print("Invalid list")
        return

    tempStack = []

    for i in range(0, n):
        tempStack.append(q.get())

    print("temp stack", tempStack)

    resultQueue = Queue()
    for i in range(0, n):
        resultQueue.put(tempStack.pop())

    #adds remaining items from original queue by dequeue

    for i in range(0, q.qsize()):
        resultQueue.put(q.get())
    print("result", resultQueue.queue)

q1 = Queue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)
q1.put(6)
q1.put(7)
q1.put(8)
q1.put(9)
q1.put(10)

reverse(q1, 5)