def Time2zero(num) :
    cnt = 0
    while num != 0 :
        num = num//10
        cnt += 1
    return cnt
a = float(input())
L = 0
U = Time2zero(a)
x = (L+U)/2
while abs(a-10**x) > (10**-10)*max(a,10**x) :
    if 10**x > a :
        L,U = L,x
    elif 10**x < a :
        L,U = x,U
    x = (L+U) / 2
print(round(x,6))