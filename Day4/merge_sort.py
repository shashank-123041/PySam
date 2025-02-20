def merge_sort(numbers, low, high):
    if low < high:
        mid = low + ((high - low) // 2)
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)

def merge(n, l, m, h):
    a1 = n[l:m+1]
    a2 = n[m+1:h+1]

    ma = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            ma.append(a1[i])
            i += 1
        else:
            ma.append(a2[j])
            j += 1
    ma += a1[i:]
    ma += a2[j:]

    for i in range(len(ma)):
        n[l + i] = ma[i]

numbers = [2, 3, 4, 1, 5, 8, 6]
merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)
