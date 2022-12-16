def reverse(d):
    ret = {}
    for key,value in d.items() :
        ret[value] = key
    return ret

def keys(d, v):
    ret = []
    for k in d :
        if d[k] == v :
            ret.append(k)
    return ret

exec(input().strip()) 
