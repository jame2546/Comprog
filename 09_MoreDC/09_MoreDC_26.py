Dcity = {}
Did = {}
res = []
for i in range(int(input())) :
    id,city = input().split(":")
    Dcity[id] = set(city.split(","))
    for t in city.split(",") :
        if t in Did :
            Did[t].append(id)
        else :
            Did[t] = [id]
find = input()
for t in Dcity[find] :
    for id in Did[t] :
        if id != find and id not in res :
            res.append(id)
if res == [] :
    print("Not Found")
else :
    print("\n".join(res))

