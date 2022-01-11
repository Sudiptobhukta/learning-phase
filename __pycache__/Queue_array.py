class Queue:
    def  __init__(self):
        self.array = []
        self.count = 0
        self._front =0

    def enqueue(self,item):
        self.array.append(item)
        self.count+=1

    def dequeue(self):
        if self.count ==0:
            return -1
        value = self.array[self._front]
        #self._front+=1
        self.count-=1
        return value

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size()==0
    
    def front(self):
        if self.count()==0:
            return -1
        return self.array[self._front]

q = Queue()
q.enqueue(45)
q.enqueue(85)
q.enqueue(96)
while q.isEmpty() is False:
    print(q.dequeue())

print(q.front())


