import sys
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

    def search(self,root,key):
        if root.key==key:
            print("Key element present in the tree!!")
        elif root.key>key:
            self.search(root.left,key)
        elif root.key<key:
            self.search(root.right,key)
        else:
            print("Key element Not present in the tree!!")
            return

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

def menu():
    obj=BST()
    root=None
    while True:
        choice=int(input("\n\n0. Exit\n1. Insert\n2. Delete\n3. Inorder\n4. Preorder\n5. Postorder\n6. LevelOrder\n7. Search\nChoice: "))
        operations={0:"",1:obj.insert,2:obj.delete,3:obj.inorder,4:obj.preorder,5:obj.postorder,6:obj.levelorder,7:obj.search}
        if choice in operations:
            match choice:
                case 0: 
                    sys.exit("Tree terminated!!")
                case 1:
                    ele=int(input("Enter the Element to insert: ")) 
                    root=operations[choice](root,ele)
                case 2:
                    key=int(input("Enter the Element to delete: ")) 
                    root=operations[choice](root,key)
                case default:
                    operations[choice](root)         
        else:
            print("Invalid Choice!!")

menu()
