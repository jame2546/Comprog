countrys = {}
list_of_teams = []
for i in range(int(input())):
    team, city = input().split()
    list_of_teams.append(team)
    if team not in countrys:
        countrys[team] = {city}
    else:
        countrys[team].add(city)
inp = input()
while inp != "q":
    check = True
    temp = []
    for team in inp.split():
        if team not in list_of_teams:
            print("Not OK")
            check = False
            break
        if countrys[team] not in temp:
            temp.append(countrys[team])
        else:
            print("Not OK")
            check = False
            break
    if check:
        print("OK")
    inp = input()
    
