line = input()
char = [line[0]]
times = []
cnt = 1
for i in range(1,len(line)) :
    if line[i-1] == line[i] :
        cnt += 1
    else :
        char.append(line[i])
        times.append(cnt)
        cnt = 1
times.append(cnt)
res = ""
for i in range(len(char)) :
    res += char[i]+" "+str(times[i])+" "
print(res.strip())