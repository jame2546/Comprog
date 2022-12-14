def onlyword(line) :
    ret = ""
    for t in line :
        if t in "(),.\"\'" :
            ret += " "
        else :
            ret += t
    return ret
find = input()
line = onlyword(input()).split()
cnt = 0
for t in line :
    if t == find :
        cnt += 1
print(cnt)