w = int(input())
if w > 2000 :
    print("Reject")
else :
    if 1000 < w <= 2000 :
        print(58)
    elif 500 < w <= 1000 :
        print(38)
    elif 250 < w <= 500 :
        print(28)
    elif 100 < w <= 250 :
        print(22)
    elif w <= 100 :
        print(18)