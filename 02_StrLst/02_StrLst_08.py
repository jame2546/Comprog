import math
a ,b ,c = input().split(",")
sed = int(a + b + c ) -int(a+b)
suan = 10**(len(b)+len(c)) - 10**(len(b))
x = math.gcd(sed , suan)
print(sed//x, '/' ,suan//x)