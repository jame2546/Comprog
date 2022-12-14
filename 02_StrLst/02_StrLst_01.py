a = input()
n = 0
for i in range(12):
    n += (13 - i) * int(a[i])
check_digit = str((11 - (n % 11)) % 10)
print(a[0] + " " + a[1:5] + " " + a[5:10] + " " + a[10:13] + " " + check_digit)