Dname = {}
Dtel = {}
for i in range(int(input())) :
    fname,lname,tel = input().split()
    Dname[fname+" "+lname] = tel
    Dtel[tel] = fname+" "+lname
for i in range(int(input())) :
    inp = input()
    if inp in Dname :
        print(inp,"-->",Dname[inp])
    elif inp in Dtel :
        print(inp,"-->",Dtel[inp])
    else :
        print(inp,"--> Not found")




