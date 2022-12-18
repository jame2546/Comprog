n = int(input())
for i in range(n) :
    line = input()
    for k in range(len(line)) :
        if line[k] != "." :
            print(line[int(k/2):])
            break