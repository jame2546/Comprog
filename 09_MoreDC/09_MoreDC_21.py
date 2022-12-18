def factor(N): 
    res = []
    for i in range(2,N,1) :
        cnt = 0
        while N % i == 0 :
            N = N/i
            cnt += 1
        if cnt != 0 :
            res.append([i,cnt])
    if res == [] :
        res = [[N,1]]
    return res

exec(input().strip())