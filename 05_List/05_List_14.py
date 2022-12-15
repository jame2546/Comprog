a = [int(e) for e in input().split()]
n = 0
for i in range(len(a)-2) :
    if a[i] < a[i+1] and a[i+1] > a[i+2] :
        n += 1 
print(n)