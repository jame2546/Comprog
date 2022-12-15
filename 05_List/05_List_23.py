def Caldistance(x,y) :
    return (x**2+y**2)**0.5
temp = []
for i in range(int(input())) :
    x,y = input().split()
    temp.append((Caldistance(float(x),float(y)),i+1,x,y))
temp.sort()
print("#"+str(temp[2][1])+":","("+str(temp[2][2])+", "+str(temp[2][3])+")")
