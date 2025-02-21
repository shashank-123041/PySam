class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end="\t")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end="\t")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end="\t")
    
    def levelorder(self,root):
        lvl=[root]
        while lvl:
            print(lvl[0].key,end="\t")
            if lvl[0].left:
                lvl.append(lvl[0].left)
            if lvl[0].right:
                lvl.append(lvl[0].right)
            lvl.pop(0)
        

    def getsucc(self,cur):
        cur=cur.right
        while cur is not None and cur.left is not None:
            cur=cur.left
        return cur

    def delete(self,root,key):
        if not root:
            print("Tree is Empty!!")
            return root
        elif root.key>key:
            root.left=self.delete(root.left,key)
        elif root.key<key:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ=self.getsucc(root)
            root.key=succ.key
            root.right=self.delete(root.right,succ.key)
        return root

root=Node(10)
obj=BST()
root=obj.insert(root,25)
root=obj.insert(root,15)
root=obj.insert(root,5)

obj.levelorder(root)