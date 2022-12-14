a = int(input())
if a < 1000 :
    print(a)
if 1000 <= a < 1000000 :
    if a <= 9999 :
        print(str(round(a/1000,1)) + 'K')
    else :
        print(str(round(a/1000)) + 'K')
if 1000000 <= a < 1000000000 :
    if a <= 9999999 :
        print(str(round(a/1000000,1)) + 'M')
    else :
        print(str(round(a/1000000)) + 'M')
if a >= 1000000000 :
    if a <= 9999999999 :
        print(str(round(a/1000000000,1)) + 'B')
    else :
        print(str(round(a/1000000000)) + 'B')