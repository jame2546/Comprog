lst = [float(e) for e in input().split()]
print(round((sum(lst)-min(lst)-max(lst))/2,2))