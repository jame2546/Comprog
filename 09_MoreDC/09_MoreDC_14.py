def getData(filename,type) :
    file = open(filename,"r")
    if type == "dict" :
        res = {}
        for line in file :
            line = line.strip()
            res[line.split(",")[0]] = line.split(",")[1]
    elif type == "list" :
        res = []
        for line in file :
            line = line.strip()
            res.append((line.split(",")[0],line.split(",")[1]))
    return res
course = getData(input(),"dict")
teacher = getData(input(),"dict")
database = getData(input(),"list")
for t in database :
    if t[0] not in course or t[1] not in teacher :
        print("record error")
    else :
        print(course[t[0]]+","+teacher[t[1]])