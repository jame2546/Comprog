M = input()
N = int(input())
if len(M) < N :
    M = "0"*(N-len(M)) + M 
print(M)