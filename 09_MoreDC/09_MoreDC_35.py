def addDict (Dict,key,value) :
    if key in Dict :
        Dict[key].add(value)
    else :
        Dict[key] = {value}
    return Dict
datas = {}
groups = {}
gens = {}
majors = {}
for i in range(int(input())) :
    name,group,gen,major = input().split() 
    groups = addDict(groups,group,name)
    gens = addDict(gens,gen,name)
    majors = addDict(majors,major,name)
    datas[name] = [group,gen,major]
Check = False
find = input().split()
tmp = set(datas.keys())
for t in find :
    if t in groups :
        tmp = tmp & groups[t]
    elif t in gens :
        tmp = tmp & gens[t]
    elif t in majors :
        tmp = tmp & majors[t]
    else :
        Check = True
if len(tmp) == 0 or Check :
    print("Not Found")
else :
    for t in sorted(list(tmp)) :
        print(t," ".join(datas[t]))



