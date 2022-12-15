import math
pars = 0
strokes = 0
im_strokes = 0
for i in range(9) :
    inp = [int(e) for e in input().split()]
    pars += inp[0]
    strokes += inp[1]
    if inp[2] :
        im_strokes += min(inp[0]+2,inp[1])
handicap = math.floor(0.8*(1.5*im_strokes - pars))
print(strokes)
print(handicap)
print(strokes-handicap)