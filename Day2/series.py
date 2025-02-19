fmemo={0:1,1:1,2:2}
pmemo={1:2}

def fib(n):
    if n in fmemo:
        return fmemo[n]
    else:
        fmemo[n]=fib(n-1)+fib(n-2)
        return fmemo[n]



"""def prime(n):
    
    if n in pmemo:
        return pmemo[n]
    else:
        for position in range(list(pmemo.keys())[-1],n+1):
            i=pmemo[position]+1
            while not isprime(i):
                i=i+1
            pmemo[position+1]=i-1
        return pmemo[n]"""

def prime(n):
    def isprime(val):
        for j in range(2,(val//2)+1):
            if val %j==0:
                return False
        return True
    if n in pmemo:
        return pmemo[n]
    else:
        last_known_prime = pmemo[len(pmemo)]
        position = len(pmemo)
        while position <= n:
            last_known_prime += 1
            while not isprime(last_known_prime):
                last_known_prime += 1
            pmemo[position + 1] = last_known_prime
            position += 1
        return pmemo[n]

number=int(input("Enter the position of the number in the series: "))
if number%2==0:
    print(prime(number//2))
else:
    print(fib((number+1)//2))

print(pmemo)
print(fmemo)