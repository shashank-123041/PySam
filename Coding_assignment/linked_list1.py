import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class Linked_list:
    
    def add_node(self,first,data):
        if first == None:
            return Node(data)
        else:
            temp=first
            while temp.link != None:
                temp=temp.link
            temp.link=Node(data)
        return first
    
    def add_position(self,first,data,pos):
        count=1
        prev,temp=None,first
        if pos<1:
            print("Invalid position!!")
            return first
        while count != pos:
            if temp==None:
                print("Invalid position!!")
                return first
            prev=temp
            temp=temp.link
            count+=1
        if count == pos:
            new=Node(data)
            new.link=temp
            prev.link=new
        return first
    
    def delete_position(self, first, pos):
        count = 1
        prev, temp = None, first
        if pos < 1 or first is None:
            print("Invalid position or empty list!!")
            return first
        while temp is not None and count < pos:
            prev = temp
            temp = temp.link
            count += 1
        if temp is None:
            print("Position out of range!")
        elif count == pos:
            if prev:
                prev.link = temp.link
            else:
                first = temp.link
        return first

    def display(self,first):
        contents=[]
        if first is None:
            print("list is empty!!")
            return
        else:
            temp=first
            while temp!=None:
                contents.append(temp.data)
                temp=temp.link
        contents.reverse()
        print(f'None<-|{contents[0]}|',end="")
        for i in range(1,len(contents)):
            print(f'|{contents[i]}|<-',end="")
        print()
        

def main():
    print("\tMenu\n0.Exit\n1.Insert\n2.Insert at a position\n3.Delete at a position\n4.Display in reverse\n")
    obj=Linked_list()
    first=None
    choice={0:"",1:obj.add_node,2:obj.add_position,3:obj.delete_position,4:obj.display}
    while True:
        ch=int(input("Choice :"))
        if ch in choice:
            match ch:
                case 1:
                    data=int(input("Enter the data to insert: "))
                    first=choice[ch](first,data)
                case 2:
                    data=int(input("Enter the data to enter: "))
                    pos=int(input("Enter the position of data to insert: "))
                    first=choice[ch](first,data,pos)
                case 3:
                    data=int(input("Enter the position to delete: "))
                    first=choice[ch](first,pos)
                case 4:
                    choice[ch](first)
                case 0:
                    sys.exit("List terminated!!")
        else:
            print("invalid choice!!")

main()