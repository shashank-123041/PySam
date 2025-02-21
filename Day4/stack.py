import sys
class Stack1:
    
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

class Stack2:
    
    def __init__(self,size=5):
        self.stk=[]
        self.size=size
        print("Empty stack is created!")

    def push(self):
        if self.size==len(self.stk):
            print("Stack overflow!!")
        else:
            ele=input("Enter the element to be pushed: ")
            self.stk.append(ele)
    
    def pop(self):
        if not self.stk:
            print("Stack Underflow!!")
        else:
            print(f"{self.stk.pop()} is popped from the stack")
    
    def display(self):
        if not self.stk:
            print("Stack Underflow!!")
        else:
            print("Stack contents: ")
            for i in range(len(self.stk)):
                print(self.stk[i])

def menu():
    cstk={1:Stack1,2:Stack2}
    ch=int(input("0.Exit\n1. Front operations\n2.Rear operations\nChoice: "))
    if ch in cstk:
        obj=cstk[ch]()
    else:
        sys.exit("Program Terminated!!")
    while True:
        choice=int(input("0. Terminate the current stack\n1. Push\n2. Pop\n3. Display\n Choice: "))
        operations={1:obj.push,2:obj.pop,3:obj.display}
        if not choice:
            break
        elif choice in operations:
            operations[choice]()
        else:
            print("Invalid Choice!!")

menu()
