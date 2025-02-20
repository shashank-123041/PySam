"""n=input("Enter the number: ")
sum=0
for i in range(0,len(n)):
    if i%2==0 and int(n[i])%2==0:
        sum+=int(n[i])
print("Sum : ",sum)"""

n=int(input("Enter the number: "))
sum=0

while n>0:
    n2=n
    d=0

    while n2>0:
        n2=n2//10
        d+=1
    
    x=n//10**(d-1)
    if d%2==0 and x%2==0:
        sum+=x
    n=n%10**(d-1)

print("Sum: ",sum)