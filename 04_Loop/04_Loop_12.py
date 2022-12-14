n = int(input())
line1 = []
line2 = []
for i in range(n) :
    a,b = input().split()
    if i % 2 == 0 :
        a,b = b,a
    line1.append(int(a))
    line2.append(int(b))
if input() == "Zig-Zag" :
    print(min(line2),max(line1))
else :
    print(min(line1),max(line2))