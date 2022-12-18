def row_number(t, e):
    for i in range(len(t)) :
        for k in range(len(t[i])) :
            if t[i][k] == e :
                return i

def flatten(t) : 
    outp = []
    for k in t :
        for num in k :
            if num != 0 :
                outp.append(num)
    return outp

def inversions(x) : 
    cnt = 0
    for i in range(len(x)) :
        for j in range(i+1,len(x)) :
            if x[i] > x[j] :
                cnt += 1
    return cnt
    
def solvable(t) : 
    if len(t) % 2 != 0 :
        if inversions(flatten(t)) % 2 == 0 :
            return True
    else :
        if inversions(flatten(t)) % 2 == 0 :
            if row_number(t,0) % 2 != 0 :
                return True
        else :
            if row_number(t,0) % 2 == 0 :
                return True
    return False

exec(input().strip())