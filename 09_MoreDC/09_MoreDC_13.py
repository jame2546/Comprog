winner = set()
loser = set()
for i in range(int(input())) :
    inp = input().split()
    winner.add(inp[0])
    loser.add(inp[1])
print(sorted(winner - loser))