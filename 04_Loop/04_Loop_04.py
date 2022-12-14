line = input()
res = ""
for char in line :
    if char in "[([" :
        res += "[(["["[(".find(char)+1]
    elif char in "])]" :
        res += "])]"["])".find(char)+1]
    else :
        res += char
print(res)