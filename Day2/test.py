num = int(input("Enter a number: "))

while num > 0:
    num2 = num
    dig = 0

    while num2 > 0:
        num2 = num2 //10
        dig = dig + 1

    x = num // 10**(dig-1)
    if dig == 1:
        print (x, end = " ")
    else:
        print (x, end = ", ")
    num = num % 10**(dig-1)