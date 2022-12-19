def SortVote(data) :
    votes = {}
    for t in data :
        if t[1] in votes :
            votes[t[1]] += int(t[2])
        else :
            votes[t[1]] = int(t[2])
    return(", ".join([t[1] for t in sorted([(v,k) for k,v in votes.items()],reverse=True)[:3]]))

def Sortota(data) :
    amt = {}
    for t in data :
        if t[1] in amt :
            amt[t[1]].add(t[0])
        else :
            amt[t[1]] = {t[0]}
    return(", ".join([t[1] for t in sorted([(len(v),k) for k,v in amt.items()],reverse=True)[:3]]))

def Sortkami(data) : 
    kami = {}
    for t in data :
        name,idol,vote = t[:]
        if name not in kami :
            kami[name] = [[-int(vote),idol]]
        else :
            run = False
            for i in range(len(kami[name])) :
                if kami[name][i][1] == idol :
                    kami[name][i][0] -= int(vote)
                    run = True
            if run == False :
                kami[name].append([-int(vote),idol])
    temp_kami = {}
    for name,lst in kami.items() :
        lst.sort()
        idol = lst[0][1]
        if idol not in temp_kami :
            temp_kami[idol] = {name}
        else :
            temp_kami[idol].add(name)
    for a in kami.values() :
        for t in a :
            if t[1] not in temp_kami :
                temp_kami[t[1]] = set()
    return ", ".join([t[1] for t in sorted([[-len(v),k] for k,v in temp_kami.items()])[:3:]])
    
inp = input().split()
Data = []
while len(inp) != 1 :
    Data.append(inp)
    inp = input().split()
cmd = inp[0]
if cmd == "1" :
    print(SortVote(Data))
elif cmd == "2" :
    print(Sortota(Data))
elif cmd == "3" :
    print(Sortkami(Data))