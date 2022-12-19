def getDirections(n) :
    Direction = []
    times = 1
    cnt = 0
    while True:
        for direc in ["R", "U", "L", "D"]:
            for i in range(times):
                Direction.append(direc)
                if len(Direction) > n**2 -1 :
                    return Direction
            cnt += 1
            if cnt == 2:
                times += 1
                cnt = 0

def spiral_square(n): # n is a positive odd number
    Matrix = [[[] for i in range(n)] for i in range(n)]
    i = n // 2 
    j = n // 2
    direction = getDirections(n) 
    for num in range(1,n*n+1) :
        Matrix[i][j] = num 
        if direction[num-1] == "R" :
            j += 1
        elif direction[num-1] == "U" :
            i -= 1
        elif direction[num-1] == "L" :
            j -= 1
        elif direction[num-1] == "D" :
            i += 1
    return Matrix
        

def print_square(S):   
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip()) 
