def arrangeStudents(a, b):
    
    def is_valid(l):
        for i in range(1, len(l)):
            if (l[i] in a and l[i-1] in a) or (l[i] in b and l[i-1] in b):
                if (l[i] in a and l[i-1] in b) or (l[i] in b and l[i-1] in a) :
                    return True
                return False
        return True
    
    arrangement=sorted(a+b)
    return is_valid(arrangement)

def main():
    t = int(input().strip())
    
    results = []
    for _ in range(t):
        n = int(input().strip())
        boys_heights = list(map(int, input().rstrip().split()))
        girls_heights = list(map(int, input().rstrip().split()))
        
        result = arrangeStudents(boys_heights, girls_heights)
        results.append("Yes" if result else "No")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
