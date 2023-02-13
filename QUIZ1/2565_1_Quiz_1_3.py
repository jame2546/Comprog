#################### VERY GOOD CREDIT TO .... ################################
line = input().replace("+", " +").replace("-", " -") ## change 3+5-3 to 3 +5 -3
print(sum([int(e) for e in line.split()])) ## change 3 +5 -3 to [3,5,-3] and find sum of this list

    