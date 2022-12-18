def first_fit(L,e): 
    for i in range(len(L)) :
        if sum(L[i]) + e <= 100 :
            L[i].append(e) 
            return L
    L.append([e])
    return L
def best_fit(L,e): 
    free = []
    for i in range(len(L)) :
        if sum(L[i]) + e <= 100 :
            free.append([[100 - (sum(L[i]) + e)],i])
    free.sort()
    if free != [] :
        L[free[0][1]].append(e)
    else :
        L.append([e])
    return L
def partition_FF(D):
    L = []
    for e in D :
        first_fit(L,e)
    return L

def partition_BF(D):
    L = [[D[0]]]
    for e in D[1:] :
        best_fit(L,e)
    return L

exec(input().strip()) 