def convex_polygon_area(p):
    n = len(p)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += p[i][0] * p[j][1]
        area -= p[j][0] * p[i][1]
    return abs(area) / 2

def is_heterogram(s):
    seen = []
    for t in s.lower() :
        if t in "aeiou" :
            if t in seen :
                return False
            else :
                seen.append(t)
    return True

def replace_ignorecase(s, a, b):
    find,line = a.lower(),s.lower()
    i = 0
    res = ""
    while i < len(s) :
        if line[i:i+len(a)] == find :
            res += b
            i += len(a)
        else :
            res += s[i]
            i += 1
    return res

def top3(votes):
    return [t[1] for t in sorted([(-v,k) for k,v in votes.items()])[:3:]]

for k in range(2):
    exec(input().strip())