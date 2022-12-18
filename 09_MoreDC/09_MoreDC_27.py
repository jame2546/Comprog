def knows(R,x,y):
    if y in R[x] :
        return True
    else :
        return False
def is_celeb(R,x): 
    for key,value in R.items() :
        if key == x :
            if value != set() and value != {x} :
                return False
        if key != x and x not in value :
            return False
    return True 
def find_celeb(R):
    for x in R :
        if is_celeb(R,x) == True :
            return x  
    return None
def read_relations() :
    R = dict()
    while True :
        d = input().split()
        if len(d) == 1 :
            break
        else :
            if d[0] not in R :
                R[d[0]] = {d[1]}
            elif d[0] in R :
                R[d[0]].add(d[1])
            if d[1] not in R :
                R[d[1]] = set()
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
 
exec(input().strip())  