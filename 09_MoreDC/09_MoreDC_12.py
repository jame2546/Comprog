n = int(input())
if n != 0 :
    union = intersect = set(input().split())
    for i in range(n-1) :
        inp = input()
        union = union | set(inp.split())
        intersect = intersect & set(inp.split())
    print(len(union))
    print(len(intersect))
else :
    print(0)
    print(0)