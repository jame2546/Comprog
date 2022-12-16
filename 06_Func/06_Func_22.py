def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def distance2(p1, p2):
    x1,y1,x2,y2 = (p1+p2)[:]
    return distance1(x1,y1,x2,y2)
    
def distance3(c1, c2):
    x1,y1,r1,x2,y2,r2 = (c1+c2)[:]
    d = distance1(x1,y1,x2,y2)
    overlap = False
    if r1 + r2 >= d :
        overlap = True
    return d,overlap

def perimeter(points):
    lengt = 0
    for i in range(len(points)) :
        lengt += distance2(points[i-1],points[i])
    return lengt


exec(input().strip())
