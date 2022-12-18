stations = {}
inp = input().split()
while len(inp) != 1:
    sta1, sta2 = inp[0], inp[1]
    if sta1 in stations:
        stations[sta1].add(sta2)
    else:
        stations[sta1] = {sta2}
    if sta2 in stations:
        stations[sta2].add(sta1)
    else:
        stations[sta2] = {sta1}
    inp = input().split()
res = set()
if inp[0] in stations:
    res.update(stations[inp[0]])
    for sta in stations[inp[0]]:
        res.update(stations[sta])
if res == set() :
    print(inp[0])
else :
    for t in sorted(res) :
        print(t)