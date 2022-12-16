Dnickname = {}
Dname = {}
for i in range(int(input())) :
    nickname,name = input().split()
    Dnickname[nickname] = name
    Dname[name] = nickname
for i in range(int(input())) :
    inp = input()
    if inp in Dnickname :
        print(Dnickname[inp])
    elif inp in Dname :
        print(Dname[inp])
    else :
        print("Not found")