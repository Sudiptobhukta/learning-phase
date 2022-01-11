from sys import stdin

class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next =  None

def odd_even(head):
    head_odd = None
    tail_odd = None
    head_even = None
    tail_even = None
    while head is not None:
        if head.data % 2 !=0:
            newnode = node(head.data)
            if head_odd is None:
                head_odd = newnode
                tail_odd = newnode
            
            else:
                tail_odd .next = newnode
                tail_odd = tail_odd.next

        else:
            newnode = node(head.data)
            if head_even == None:
                head_even = newnode
                tail_even = newnode
            
            else:
                tail_even.next = newnode
                tail_even= tail_even.next

        head= head.next

    if tail_odd == None:
        return head_even
    else:
        tail_odd.next = head_even
        return head_odd


def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = odd_even(head)
    printLinkedList(newHead)  
    
    t -= 1