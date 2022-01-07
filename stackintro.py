class stackcheck:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey this is end of stack")
            return

        return self.data.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.data)
    
    def top(self):
        if self.isEmpty():
            print("Hey this stack is empty")

        return self.data[len(self.data)-1]

        