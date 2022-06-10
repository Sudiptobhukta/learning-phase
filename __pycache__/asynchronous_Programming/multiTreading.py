import queue
from threading import Thread

def producer(q):
    for i in range(4):
        q.put(i)
        print("Produced: ",i)

def consumed(q):
    while True:
        data= q.get()
        print("consumed: ",data)

q= queue.Queue()

Produced = Thread(target=producer,args=(q,))
Consumed = Thread(target=consumed,args=(q,))

Consumed.start()
Produced.start()
