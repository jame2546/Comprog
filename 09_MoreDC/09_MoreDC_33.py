def sum_poly(p) : 
    p = [[x,y] for x,y in p]
    for i in range(len(p)) : 
        ind = p[i][1]
        for j in range(i+1,len(p)) :
            if ind == p[j][1] :
                p[i][0] += p[j][0]
                p[j][0] = 0
    return [(y,x) for x,y in sorted([(y,x) for x,y in p if x != 0],reverse=True) ]

def add_poly(p1, p2):
    return sum_poly(p1+p2)

def mult_poly(p1, p2):
    p = []
    for x in p1 :
        for y in p2 :
            p.append((x[0]*y[0],x[1]+y[1]))
    return sum_poly(p)

for i in range(3):
    exec(input().strip())
