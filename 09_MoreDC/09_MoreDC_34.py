def pattern1(nrows, ncols):
    Matrix = [[] for i in range(nrows)]
    j = 0
    for i in range(1,nrows*ncols+1) :
        Matrix[j].append(i)
        if len(Matrix[j]) == ncols :
            j += 1
    return Matrix


def pattern2(nrows, ncols):
    Matrix = [[] for i in range(nrows)]
    j = 0
    for i in range(1,nrows*ncols+1) :
        Matrix[j].append(i)
        j += 1
        if j == nrows :
            j = 0
    return Matrix

def pattern3(N):
    Matrix = [[0] * N for i in range(N)]
    value = 1
    for i in range(N):
        for j in range(i, N):
            Matrix[i][j] = value
            value += 1
    return Matrix
            
def pattern4( N ): 
    Copy = [[] * N for i in range(N)]
    Matrix = [[] * N for i in range(N)]
    k = 0
    for i in range(1,int(N*(N+1)/2)+1) :
        Copy[k].append(i)
        if len(Copy[k]) == k+1 :
            for i in range(N - k - 1) :
                Copy[k].insert(0,0)
            Copy[k] = Copy[k][::-1]
            k += 1
    for i in range(N) :
        for t in Copy :
            Matrix[i].append(t[i])
    return Matrix

def pattern5( N ):
    Matrix = [[] * N for i in range(N)]
    j = 0
    k = 0
    for i in range(1,int(N*(N+1)/2)+1) :
        Matrix[j].append(i)
        j += 1
        if j == N - k :
            k += 1
            j = 0
    for i in range(len(Matrix)) :
        while len(Matrix[i]) != N :
                Matrix[i].insert(0,0)
    return Matrix

def pattern6( N ):
    Matrix = [[] for i in range(N)]
    switch = True
    t = 0
    j = 0
    k = -2
    p = 1
    for i in range(1,int(N*(N+1)/2)+1) :
        if switch :
            Matrix[j].append(i)
            j += 1
            if j == N  - 2*t :
                t += 1
                j = 0
                switch = False
        else :
            Matrix[k].append(i)
            k -= 1
            if k == -N -1 :
                p += 1
                k = -2*p
                switch = True
    for i in range(len(Matrix)) :
        while len(Matrix[i]) != N :
                Matrix[i].insert(0,0)
    return Matrix

exec(input().strip()) 