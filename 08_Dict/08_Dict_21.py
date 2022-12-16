line = input().lower()
D = {}
for ch in line :
    if ch not in "0123456789" :
        if ch not in D and ch not in ["+","-","*","/"," "] :
            D[ch] = 1
        elif ch not in ["+","-","*","/"," "]:
            D[ch] += 1
tmp = []
for k,v in D.items() :
    tmp.append([-v,k])
for t in sorted(tmp) :
    print(t[1],"->",str(-t[0]))