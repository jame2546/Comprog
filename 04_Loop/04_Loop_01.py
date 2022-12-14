inp = input()
tmp = []
while inp != "q" :
    tmp.append(float(inp))
    inp = input()
if len(tmp) > 0 :
    print(round(sum(tmp)/len(tmp),2))
else :
    print("No Data")