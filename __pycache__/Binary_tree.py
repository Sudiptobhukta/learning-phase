from tkinter.messagebox import NO


class binarytree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

# taking the input into binary tree

def inputree():
    inroot = int(input())
    if inroot == -1:
        return None

    root = binarytree(inroot)
    leftroot = inputree()
    rightroot = inputree()
    root.left = leftroot
    root.right = rightroot
    return root

#printing the data in detailed form    

def detailprint(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left!= None:
        print('L', root.left.data , end=",")
    if root.right!= None:
        print('R', root.right.data,end="")

    print()
    detailprint(root.left)
    detailprint(root.right)

# to count the nodes of tree

def numnode(root):
    if root == None:
        return 0

    left = numnode(root.left)
    right = numnode(root.right)
    return 1+ left + right

# printing the node pre order wise

def preorder(root):
    if root == None:
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

# printing the node post order

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")


# largest data in the tree

def largestdata(root):
    if root == None:
        return -1
    left = largestdata(root.left)
    right = largestdata(root.right)
    large = max(left , right , root.data)
    return large

# largest no. than x

def largestx(root,x):
    if root == None:
        return 0
    left = largestx(root.left,x)
    right = largestx(root.right,x)
    if x < root.data:
        return 1+ left +right
    return left + right

# height of tree

def height(root):
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)
    if left > right:
        return 1+ left
    else:
        return 1+ right

# Number of leaf Node

def numb(root):
    if root ==  None:
        return 0
    if root.left == None and root.right == None:
        return 1
    left = numb(root.left)
    right = numb(root.right)
    return left + right

# print the depth of the tree (k is for depth)

def depth1(root,k):
    if root == None:
        return
    if k ==0:
        print(root.data,end=" ")
    depth1(root.left,k-1)
    depth1(root.right,k-1)

# depth2 in the second way

def depth2(root,k,d):
    if root == None:
        return
    if k ==d:
        print(root.data,end=" ")
    depth2(root.left,k,d+1)
    depth2(root.right,k,d+1)

root = inputree()
detailprint(root)
numnode(root)
postorder(root)
print()
print(largestdata(root))
print(largestx(root,3))
print(height(root))
print(numb(root))
depth1(root,2)
depth2(root,2,0)