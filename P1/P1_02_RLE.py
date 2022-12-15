def str2RLE(s):
    out = ""
    c = s[0]
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == c:
            cnt += 1
        else:
            out += c + " " + str(cnt) + " "
            c = s[i]
            cnt = 1
    out += c + " " + str(cnt)
    return out

def RLE2str(s) :
    s = s.split()
    out = ""
    for i in range(1,len(s),2) :
        out += s[i-1]*int(s[i])
    return out
oper = input()
if oper == "str2RLE" :
    print(str2RLE(input()))
elif oper == "RLE2str" :
    print(RLE2str(input()))
else :
    print("Error")