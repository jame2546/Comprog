"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠈⡯⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡞⣺⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠏⠎⢟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢠⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣮⣇⢾⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠴⠒⢲⡿⣿⣟⣾⠀⢀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⣈⡥⡂⢸⣆⠓⣁⢻⡏⠁⠹⣓⠄⠀⠀⠀
⠀⠀⠀⠀⠀⢰⡥⣖⣠⣾⡿⢽⣁⢺⡇⠀⣴⡒⣦⢄⡀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣳⣿⡟⣿⡦⢩⡧⣴⣖⡷⡃⠀⢹⣧
⠀⠀⢀⠠⠆⣿⣿⣻⣿⣿⣿⣿⣿⣭⣿⣿⢧⣹⣧⣴⣾⣿
⢀⠇⠀⡀⢸⣿⢿⡿⣟⣯⣵⣻⣿⣗⣿⣿⣽⣷⣿⣿⡿⣽
⠈⣜⠀⠀⣞⢙⢏⢿⣿⣷⡡⣏⣻⣏⣌⣿⣛⣳⣿⣿⡿⣽
⠀⢺⣥⡿⡔⣀⢮⣜⣿⣿⣫⡿⢳⡿⣻⣝⡾⢻⣹⣻⣿⣿
⠀⠘⣿⣿⣱⡵⡯⣽⣿⣿⣷⠧⠭⠕⡣⡚⡞⢯⣷⣿⣽⣿
⠀⠀⠘⣿⣿⣿⣿⣽⣿⣿⣷⢟⣾⣖⡧⣗⣺⣹⣾⠳⣿⡿
⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣇⣟⣟⣛⢇⣼⣿⡇
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣻⣿⣻⣽⣿⣺⣎⣣⣿⣾⣿⠇
⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⢿⡿⣻⣾⢿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡿⣟⣿⡏⢿⣿⢿⢿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀
"""

def dayDelivered(op,date) :
    days = {"E":1,"Q":3,"N":7,"F":14}
    return add_days(date,days[op])

def add_days(date, num_days):
    
    def days_in_month(year, month):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month in [4, 6, 9, 11]:
            return 30
        if month == 2:
            if leapyear(year):
                return 29
            else:
                return 28
        return 0

    def add_one_month(year, month):
        if month == 12:
            return year + 1, 1
        return year, month + 1

    d, m, y = date[:]
    while num_days != 0:
        if num_days > 0:
            days_in_current_month = days_in_month(y, m)
            if d + num_days > days_in_current_month:
                num_days -= (days_in_current_month - d + 1)
                d = 1
                y, m = add_one_month(y, m)
            else:
                d += num_days
                num_days = 0
        else:  # num_days < 0
            if d + num_days < 1:
                y, m = add_one_month(y, m - 1)
                days_in_prev_month = days_in_month(y, m)
                num_days += days_in_prev_month
                d = days_in_prev_month + num_days + 1
            else:
                d += num_days
                num_days = 0
    return y, m, d 

def Error(date,op) :
    d,m,y = date[:]
    if y < 2558 :
        return True,"Invalid year"
    if m not in [1,2,3,4,5,6,7,8,9,10,11,12] :
        return True,"Invalid month"
    if d <= 0 :
        return True,"Invalid date"
    if m in [1,3,5,7,8,10,12] :
        if d > 31 :
            return True,"Invalid date"
    if m in [4,6,9,11] :
        if d > 30 :
            return True,"Invalid date"
    if m == 2 :
        if leapyear(y) == True :
            if d > 29 :
                return True,"Invalid date"
        else :
            if d > 28 :
                return True,"Invalid date"
    if op not in ["E","Q","N","F"] :
        return True,"Invalid delivery type"
    return False,"FCK"

def leapyear(y):
    y = y - 543
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


list_error = []
delivered = []
inp = input()
while inp != "END" :
    inp = inp.split()
    q,op,date = inp[0],inp[1],inp[2:]
    date = [int(e) for e in date[:]]
    if Error(date,op)[0] :
        list_error.append((q,op,date,Error(date,op)[1]))
    else :
        delivered.append((dayDelivered(op,date),q))
    inp = input()
for t in list_error :
    print("Error:",t[0],t[1],t[2][0],t[2][1],t[2][2],"-->",t[-1])
for t in sorted(delivered) :
    print(t[1]+": delivered on "+"/".join([str(e) for e in t[0][::-1]]))
