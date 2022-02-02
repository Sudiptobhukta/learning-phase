import queue

#this is queue example FIFO
q = queue.Queue()
q.put(1)
q.put(5)
q.put(6)
q.put(7)
while not q.empty():
    print(q.get())

print(" ")
#this is stack inbuilt example LIFO
q1= queue.LifoQueue()
q1.put(1)
q1.put(2)
q1.put(3)
q1.put(6)
while not q1.empty():
    print(q1.get())