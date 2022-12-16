def missing_digits(t):
    num = ['0','1','2','3','4','5','6','7','8','9']
    for e in t : 
        if e in num :
            num.remove(e)
    num = [int(e) for e in num]
    return num
        

exec(input()) # DON'T remove this line
