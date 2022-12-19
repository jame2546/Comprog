def LSTRIP(filename) :
    outp = []
    file = open(filename,"r")
    cnt = []
    for line in file :
        for i in range(len(line.strip())) :
            if line[i] != "." :
                cnt.append(i)
                break
    ind = min(cnt)
    file = open(filename,"r")
    for line in file :
        outp.append(line[ind:])
    return outp

def RSTRIP(filename) :
    outp = []
    file = open(filename,"r") 
    cnt = []
    for line in file :
        for i in range(1,len(line.strip())) :
            if line[i-1] != "." and line[i] == "." :
                cnt.append(i)
    ind = max(cnt)
    file = open(filename,"r") 
    for line in file :
        outp.append(line[:ind])
    return outp

def STRIP(filename) :
    outp = []
    file = open(filename,"r")
    cnt = []
    for line in file :
        for i in range(len(line.strip())) :
            if line[i] != "." :
                cnt.append(i)
                break
    Firstind = min(cnt)
    file = open(filename,"r") 
    cnt = []
    for line in file :
        for i in range(1,len(line.strip())) :
            if line[i-1] != "." and line[i] == "." :
                cnt.append(i)
    Lastind = max(cnt)
    file = open(filename,"r") 
    for line in file :
        outp.append(line[Firstind:Lastind])
    return outp

def STRIP_ALL(filename) :
    outpP = []
    file = open(filename,"r")
    temp = set()
    cnt = 0
    for line in file :
        if cnt == 0 :
            for i in range(len(line)) :
                temp.add(i)
            cnt += 1
        else :
            for i in range(len(line)) :
                if line[i] != "." and i in temp :
                    temp.remove(i)
    file = open(filename,"r")
    for line in file :
        outp = ""
        for i in range(len(line.strip())) :
            if i not in temp :
                outp += line[i]
        outpP.append(outp)
    return outpP
def Print(lst) :
    for line in lst :
        print(line.strip())
fname = input().strip()
operation = input()
if operation == "LSTRIP" :
    Print(LSTRIP(fname))
elif operation == "RSTRIP" :
    Print(RSTRIP(fname))
elif operation == "STRIP" :
    Print(STRIP(fname))
elif operation == "STRIP_ALL" :
    Print(STRIP_ALL(fname))
else :
    print("Invalid command")