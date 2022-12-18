Capa = {}
Dict = {}
for i in range(int(input())) :
    major,max = input().split()
    Capa[major] = int(max)
for i in range(int(input())) :
    data = input().split()
    id,gpa,major = data[0],data[1],data[2:]
    Dict[float(gpa)] = [id,major]
data = []
for t in sorted(Dict.keys(),reverse=True) :
    id,major = Dict[t]
    for m in major :
        if Capa[m] >= 1 :
            data.append([id,m])
            Capa[m] -= 1
            break
for t in sorted(data) :
    print(t[0],t[1])