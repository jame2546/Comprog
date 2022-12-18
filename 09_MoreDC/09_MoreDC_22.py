def read_matrix() :
    m = []
    nrows = int(input())
    for k in range(nrows) :
        x = input().split()
        r = []
        for e in x :
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c,A) :
    for row in A :
        for j in range(len(row)) :
            row[j] = c*row[j]
    return A

def mult(A,B) :
    c = []
    d = []
    n = 0
    for i in range(len(A)) :
        for j in range(len(B[0])) :
            for k in range(len(A[0])) :
                 n += A[i][k]*B[k][j]
            c.append(n)
            n = 0
        d.append(c)
        c = []    
    return d    

exec(input().strip())