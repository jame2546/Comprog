n = int(input())
num = [str(n)]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    num.append(str(n))
if len(num) <= 15 :
    print("->".join(num))
else :
    print("->".join(num[-15:]))