first = "abcdefghijklm"
last = "nopqrstuvwxyz"
sentence = input()
outp = ""
while sentence != "end" :
    for t in sentence :
        if t in first :
            outp += last[first.find(t)]
        elif t in first.upper() :
            outp += last.upper()[first.upper().find(t)]
        elif t in last :
            outp += first[last.find(t)] 
        elif t in last.upper() :
            outp += first.upper()[last.upper().find(t)]
        else :
            outp += t
    print(outp)
    outp = ""
    sentence = input()