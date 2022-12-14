def day_of_year(d, m, y):
 # d, m, y เป็นจ ำนวนเต็มเก็บเลขวัน เลขเดือน และเลขปี พ.ศ. ตำมล ำดับ
 # คืน เลขวันที่ของปี ของวันเดือนปีที่ได้รับ
    
    
    return int(d) + daystomonth(m,y) 

def leap_years(y):
    leap = False
    y = int(y) - 543
    if y % 4 == 0 :
        leap = True
        if y % 100 == 0 :
            leap = False
            if y % 400 == 0 :
                leap = True
    return leap
def dayinfreb(y):
    if leap_years(y) == True :
        return 29
    else :
        return 28
def daystomonth(m,y):
    daysinmonth = [0,31,dayinfreb(y),31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(m) :
        days += daysinmonth[i]
    return days
    
        
    
    
        
exec(input()) # DON'T remove this line