line = [int(e) for e in input().split()]
repeated = set()
for t in line :
    repeated.add(int(t))
print(len(repeated))
print(sorted(repeated)[:10])