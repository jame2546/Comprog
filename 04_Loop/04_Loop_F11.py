def RLE(t):
    if t == "" :
        return []
    else :
        word = [t[0]]
        times = []
        cnt = 1
        for i in range(1,len(t)) :
            if t[i-1] == t[i] :
                cnt += 1
            else :
                word.append(t[i]) 
                times.append(cnt)
                cnt = 1
        times.append(cnt)
        p = []
        for i in range(len(word)) :
            p.append([str(word[i]),int(times[i])])
        return p
exec(input()) # DON'T remove this line