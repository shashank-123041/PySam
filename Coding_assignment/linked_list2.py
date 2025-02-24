import sys
import linked_list1
from linked_list1 import add_node

def create_list(list,n):
    for i in range(n):
        ip=int(input("Enter the number to insert: "))
        list=add_node(list,ip)
    return list

def check(list1,list2):
    t1=list1
    t2=list2
        
    while t1 is not None:
        if t1.val == t2.val:
            break
        t2=list2
        while t2 is not None:
            if t2.val!=t1.val:
                t2=t2.link
            else:
                break
    
    while t1 is not None and t2 is not None:
        if t1.val!=t2.val:
            return False
    return True

list1=list2=None
n1=int(input("Enter the number of nodes in list1: "))
create_list(list1,n1)
n2=int(input("Enter the number of nodes in list1: "))
create_list(list2,n2)
result=check(list1,list2)
if result:
    print("Lists' converge")
else:
    print("Lists' don't converge")