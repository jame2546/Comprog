def check_digit(n):
    a = 0
    for i in range(12):
        a = (13-i)*int(n[i]) + a
    b = str((11 - (a)%11)%10)
    return b  



exec(input()) # DON'T remove this line