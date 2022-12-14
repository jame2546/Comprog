line1 = ""
line2 = ""
n = input()
k = 0
while n != "Zig-Zag" and n != "Zag-Zig" :
    if k % 2 == 0 : 
        line1 = line1 + " " + str(n.split()[0])
        line2 = line2 + " " + str(n.split()[1])
    else :
        line1 = line1 + " " + str(n.split()[1])
        line2 = line2 + " " + str(n.split()[0])
    k += 1
    n = input()
line1 = [int(e) for e in line1.split()]
line2 = [int(e) for e in line2.split()]
if n == "Zig-Zag" :
    print(min(line1),max(line2))
else :
    print(min(line2),max(line1))