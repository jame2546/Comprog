def ReadVector(vector) :
    vector = vector[1:len(vector)-1]
    return [float (e) for e in vector.split(",")]
def AddVector(u,v) :
    return list((u[0]+v[0],u[1]+v[1],u[2]+v[2]))
u = ReadVector(input())
v = ReadVector(input())
print(u,"+",v,"=",AddVector(u,v))