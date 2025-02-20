class Stack:
    
    def __init__(self,size=5):
        self.stk=[]
        self.size=size
        print("Empty stack is created!")

    def push(self):
        if self.size==len(self.stk):
            print("Stack overflow!!")
        else:
            ele=input("Enter the element to be pushed: ")
            self.stk.insert(0,ele)
    
    def pop(self):
        if not self.stk:
            print("Stack Underflow!!")
        else:
            print(f"{self.stk[0]} is popped from the stack")
            del(self.stk[0])
    
    def display(self):
        if not self.stk:
            print("Stack Underflow!!")
        else:
            print("Stack contents: ")
            for i in range(len(self.stk)):
                print(self.stk[i])
