d = int(input())
m = int(input())
y = int(input()) - 543

if y % 400 == 0:
    leap = True
elif y % 100 == 0:
    leap = False
elif y % 4 == 0:
    leap = True
else:
    leap = False

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if leap:
    day_in_month[1] = 29

day_before = 0
for i in range(m-1):
    day_before += day_in_month[i]

output = d + day_before

print(output)
