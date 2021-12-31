class node:
    def __init__(self,data) -> None:
        self.data= data
        self.next = None

def insertinglist():
    list=[int(i) for i in input().split(" ")]
    head = None
    tail = None
    for inputdata in list:
        if inputdata == -1:
            break
        newnode= node(inputdata)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode
    return head

def findnode(head,n):
    if head is None:
        return -1
    if head.data == n:
        return 0
    find = findnode(head.next,n)
    if find== -1:
        return -1
    else:
        return find+1

def printll(x):
    while x is not None:
        print(str(x.data) +'-:>',end=(" "))
        x=x.next
    print(None)
    return

head= insertinglist()
printll(head)
print(findnode(head,4))
