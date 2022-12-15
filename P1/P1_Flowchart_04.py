x1 = str(input().strip())
x2 = str(input().strip())
x3 = str(input().strip())
x = x1 + x2 + x3
if len(x) == 9 :
    win = "-"
    i = 0
    while i < 3 :
        if x[3*i] == x[3*i+1] == x[3*i+2] :
            win = x[3*i]
            break
        elif x[i] == x[i+3] == x[i+6] :
            win = x[i]
            break
        i += 1
    if "-" in win :
        if x[0] == x[4] == x[8] :
            win = x[0]
        if x[3] == x[4] == x[6] :
            win = x[6]
    if "-" in win :
        print("???")
    else :
        print(win)
else :
    print("ERROR")