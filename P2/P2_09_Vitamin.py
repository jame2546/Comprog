def Show(list):
    [print(t[0], " ".join([str(t) for t in t[1]])) for t in list]

def Get(name, list):
    res = [t[0] + " " + " ".join([str(t) for t in t[1]]) for t in list if t[0] == name]
    return res[0] if res else name + " not found"

def Average(type, list):
    data = [t[1][type - 1] for t in list]
    return round(sum(data) / len(data), 4)

def Max(type, list):
    data = [t[1][type - 1] for t in list]
    res = [t[0] + " " + str(t[1][type - 1]) for t in sorted(list) if t[1][type - 1] == max(data)]
    return res[0]

def Sort(type, list):
    data = [[t[1][type - 1], t[0]] for t in list]
    return " ".join([t[1] for t in sorted(data)])

lst = []
for i in range(int(input())) :
    inp = input().split()
    lst.append([inp[0],[float(e) for e in inp[1:]]])
cmd = input().split()
if cmd[0] == "show" :
    Show(lst)
elif cmd[0] == "get" :
    print(Get(cmd[1],lst))
elif cmd[0] == "avg" :
    print(Average(int(cmd[1]),lst))
elif cmd[0] == "max" :
    print(Max(int(cmd[1]),lst))
elif cmd[0] == "sort" :
    print(Sort(int(cmd[1]),lst))