temp = []
for i in range(int(input())) :
    temp.append(input())
temp += [e for e in input().split()]
inp = input()
while inp != "-1" :
    temp.append(inp)
    inp = input()
res = []
for i in range(len(temp)) :
    if i % 2 == 0 :
        res.append(int(temp[i]))
    else :
        res.insert(0,int(temp[i]))
print(res)