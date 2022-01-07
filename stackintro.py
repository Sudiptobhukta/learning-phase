class stack:
    def __init__(self) -> None:
        self.data= []
    
    def push(self,item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            print('Hey stack is empty')
            return
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            print(" Hey stack is Empty")
            return 
        return self.data[len(self.data)-1]

    def isEmpty(self):
        if self.size()==0:
            return ("hey it empty")
    
    def size(self):
        return len(self.data)
        