# this is a linked list
class node:
    def __init__(self,data) -> None:
        self.data= data
        self.next=None
# this is input taking
def inputlist():

    inputl= [int(i) for i in input().split(" ")]
    head = None
    tail = None
    for inputdata in inputl:
         if inputdata == -1: break

         newnode = node(inputdata)
         if head is None:
             head= newnode
             tail = newnode
         else:
             tail.next = newnode
             tail = newnode

    return head

# this is printing
def printll(x):
    while x is not None:
        print(str(x.data) + '-:>', end=" ")
        x= x.next
    return 

head = inputlist()
printll(head)