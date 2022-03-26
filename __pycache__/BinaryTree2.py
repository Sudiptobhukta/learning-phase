class binarynode:
    def __init__(self,data) -> None:
        self.data= data
        self.left = None
        self.right = None
    
class bst:
    def __init__(self) -> None:
        self.root = None
        self.numnode = 0

    def printtree(self):
        self.printtreehelper(self.root)

    def printtreehelper(self,root):
        if root == None:
            return
        print(root.data,end=":")
        if root.left != None:
            print("L:",root.left.data,end=",")
        if root.right != None:
            print("R:",root.right.data,end="")
        print()
        self.printtreehelper(root.left)
        self.printtreehelper(root.right)

    def search(self,data):
        return self.searchelper(self.root,data)
    
    def searchelper(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            return self.searchelper(root.left,data)
        if root.data < data:
            return self.searchelper(root.right,data)

    def insert(self,data):
        newnode= self.inserthelper(self.root,data)
        self.root = newnode

    def inserthelper(self,root,data):
        if root == None:
            node = binarynode(data)
            return node
        if root.data > data:
            root.left = self.inserthelper(root.left,data)
            return root 
        if root.data < data:
            root.right = self.inserthelper(root.right,data)
            return root

    def delete(self,data):
        deleted,newnode = self.deletehelper(self.root,data)
        self.root = newnode
        return deleted

    def deletehelper(self,root,data):
        if root is None:
            return False,None
        if root.data>data:
            deleted,newnode = self.deletehelper(root.left,data)
            root.left = newnode
            return deleted,root
        if root.data<data:
            deleted, newnode = self.deletehelper(root.right,data)
            root.right = newnode
            return deleted,root
        if root.left == None and root.right == None:
            return True, None
        if  root.left is None:
            return True,root.right
        if root.right  is None:
            return True,root.left
        replacement =  self.mini(root.right)
        root.data = replacement
        deleted,newnode =  self.deletehelper(root.right,replacement)
        root.right = newnode
        return True , root

