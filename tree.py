class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if(self.data==None):
            self.data=None
        else:
            if(data<self.data):
                if(self.left==None):
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.right==None):
                    self.right=node(data)
                else:
                    self.right.insert(data)
    def preorder(self,root):
        res=[]
        if(root):
            res.append(root.data)
            res+=self.preorder(root.left)
            res+=self.preorder(root.right)
        return res
    def inorder(self,root):
        res=[]
        if(root):
            res+=self.inorder(root.left)
            res.append(root.data)
            res+=self.inorder(root.right)
        return res
    def postorder(self,root):
        res=[]
        if(root):
            res+=self.postorder(root.left)
            res+=self.postorder(root.right)
            res.append(root.data)
        return res
n=int(input("enter the no of nodes:"))
r=int(input("enter the root of the tree:"))
root=node(r)
for i in range(n-1):
    r=int(input(f"enter the value{i+1}:"))
    root.insert(r)
print("the preorder traversal of the tree is :",root.preorder(root))
print("the inorder traversal of the tree is :",root.inorder(root))
print("the postorder traversal of the tree is :",root.postorder(root))

