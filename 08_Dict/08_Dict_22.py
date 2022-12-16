def Topsales(ice_cream_sales) :
    tmp = []
    for k,v in ice_cream_sales.items() :
        tmp.append([v,k])
    tmp.sort()
    Top = [tmp[0][1]]
    for t in tmp :
        if t[0] == tmp[0][0] and t[1] != tmp[0][1] :
            Top.append(t[1])
    return sorted(Top)
    
ice_cream = {}
ice_cream_sales = {}
for i in range(int(input())) :
    name,price = input().split()
    ice_cream[name] = float(price)

for i in range(int(input())) :
    name,amt = input().split()
    if name in ice_cream :
        if name in ice_cream_sales :
            ice_cream_sales[name] += -int(amt)*ice_cream[name]
        else :
            ice_cream_sales[name] = -int(amt)*ice_cream[name]
        
if ice_cream_sales == {} :
    print("No ice cream sales")
else :
    print("Total ice cream sales:",str(-sum(ice_cream_sales.values())))
    print("Top sales:",", ".join(Topsales(ice_cream_sales)))