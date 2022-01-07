


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class stackll:

    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def push(self,item):
        newhead = Node(item)
        newhead.next = self.head
        self.head = newhead
        self.count +=1

    def pop(self):
        if self.isEmpty() is True:
            print("Hey stack is empty")
            return
        data = self.head.data
        self.head = self.head.next
        self.count-=1
        return data

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size()==0

    def top(self):
        if self.isEmpty() is True:
            print("Hey stack is empty")
            return
        return self.head.data

s = stackll()
s.push(45)
s.push(12)
s.push(86)
while s.isEmpty() is False:
    print(s.pop())
s.top()