def bubble_sort(numbers):
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if(numbers[j]>numbers[j+1]):
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
n=[2, 3, 4, 1, 5, 8, 6]
bubble_sort(n)
print(n)