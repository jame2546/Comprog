M,N,K = [int(e) for e in input().split()]
bandit_fac = dict()
guest_fac = dict()
for _ in range(M) :
    bandit,facult = input().split()
    bandit_fac[bandit] = facult
for _ in range(N) :
    inp = input().split()
    guest,bandits = inp[0],inp[1:]
    guest_fac[guest] = set()
    for bandit in bandits :
        guest_fac[guest].add(bandit_fac[bandit])
for _ in range(K) :
    inp = input().split()
    tmp = guest_fac[inp[0]]
    for t in inp[1:] :
        tmp = tmp.intersection(guest_fac[t])
    if tmp == set() :
        print("None")
    else :
        print(" ".join(sorted(tmp)))   
