def days_in_months(year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        days_in_month[2] = 29
    return days_in_month

def leap_year(year):
    year -= 543
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def Redline(d,m,y) :
    days_in_month = days_in_months(y)
    days_remain = sum(days_in_month[m+1:])
    return days_in_month[m] - d + 1 + days_remain

def Blackline(by,y) :
    return (y-by-1)*365

def Blueline(d,m,y) :
    days_in_month = days_in_months(y)
    days_before = sum(days_in_month[:m])
    return  d - 1 + days_before


bd, bm, by, d, m, y = [int(e) for e in input().split()]

t = Redline(bd,bm,by) + Blackline(by,y) + Blueline(d,m,y)
import math
sin = lambda t,dec : math.sin(2 * math.pi * t / dec)
print(t,
    "{:.2f}".format(sin(t,23)),
    "{:.2f}".format(sin(t,28)),
    "{:.2f}".format(sin(t,33)))