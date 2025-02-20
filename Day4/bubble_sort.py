
def bubble_sort(numbers):
    global count
    count=0
    for i in range(0,len(numbers)-1):
        sorted=True
        for j in range(0,len(numbers)-i-1):
            count+=1
            if(numbers[j]>numbers[j+1]):
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
                sorted=False
        if sorted:
            #print(count)
            return

n=[6,5,4,3,2,1]
bubble_sort(n)
print(n,count)