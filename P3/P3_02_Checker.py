Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Check(row,col) :
    Checkrow = True
    Checkcol = True
    if row.upper() not in list(Alphabets) :
        Checkrow = False
    if len(col) == 0 :
        Checkcol = False
    if Checkcol == True : 
        for t in col : 
            if t not in "0123456789" :
                Checkcol = False
                break
        if Checkcol == True :
            if not 1 <= int(col) <= 52 :
                Checkcol = False
    if Checkrow == False and Checkcol == False :
        return "Invalid row and column"
    elif Checkrow == False :
        return "Invalid row"
    elif Checkcol == False :
        return "Invalid column"
    return True
def Findcolor(row,col) :
    Nrow = int(Alphabets.find(row.upper()))
    Ncol = int(col) - 1
    if ( Nrow + Ncol ) % 2 == 0 :
        return "White"
    else :
        return 'Black'

inp = input().split(",")
if len(inp) == 1 :
    row = inp[0][0]
    col = inp[0][1:]
    if Check(row.strip(),col.strip()) == True :
        print(Findcolor(row,col))
    else :
        print(Check(row.strip(),col.strip()))
else :
    if inp[0].split("=")[0].strip() == "col" :
        col = inp[0].split("=")[1].strip()
        row = inp[1].split("=")[1].strip()
    else :
        col = inp[1].split("=")[1].strip()
        row = inp[0].split("=")[1].strip()
    if Check(row.strip(),col.strip()) == True :
        print(Findcolor(row,col))
    else :
        print(Check(row.strip(),col.strip()))