name1,month1,day1,year1 = input().split()
name2,month2,day2,year2 = input().split()
month = ["December","November","October","September","August","July","June","May","April","March","February","January"]
date1 = [int(month.index(month1)),day1[0:len(day1)-1]]
date2 = [int(month.index(month2)),day2[0:len(day1)-1]]
if int(year1) > int(year2) :
    print(name2)
if int(year1) < int(year2) :
    print(name1)
if int(year1) == int(year2) :
    if date1 > date2 :
        print(name1)
    elif date1 < date2 :
        print(name2)
    else :
        print(name1,name2)