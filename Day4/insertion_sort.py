s = input("Enter the string to sort: ")

def compare(ch1, ch2):
    ch1 = ch1.lower()
    ch2 = ch2.lower()
    if ch1 < ch2:
        return True
    return False

s = list(s)

for i in range(1, len(s)):
    letter = s[i]
    j = i - 1
    while j >= 0 and compare(letter, s[j]):
        s[j + 1] = s[j]
        j -= 1
    s[j + 1] = letter

print("Sorted string:", ''.join(s))
