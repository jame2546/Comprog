def is_odd(n):
    return bool(n % 2)

def has_odds(x):
    for t in x :
        if is_odd(t) :
            return True
    return False

def all_odds(x):
    for t in x :
        if not is_odd(t) :
            return False
    return True

def no_odds(x):
    for t in x :
        if is_odd(t) :
            return False
    return True

def get_odds(x):
    ret = list()
    for t in x :
        if is_odd(t) :
            ret.append(t)
    return ret

def zip_odds(a, b):
    A,B = get_odds(a),get_odds(b)
    passed = []
    for i in range(len(A)+len(B)) :
        if i < len(A) :
            passed.append(A[i])
        if i < len(B) :
            passed.append(B[i])
    return passed

exec(input().strip()) 