def getData (filename) :
    Data = []
    file = open(filename,"r")
    for line in file :
        id,grade = line.strip().split()
        fac = int(id[-2:])
        Data.append([fac,id,grade])
    return Data
name1,name2 = input().split()
Data = sorted(getData(name1) + getData(name2))
for t in Data :
    print(t[1],t[2])
