def make_int_list(x):
    return [int(e) for e in x.split()]

def is_odd(e):
    return bool(e % 2)

def odd_list(alist):
    tmp = []   
    for t in alist :
        if is_odd(t) :
            tmp.append(t)
    return tmp

def sum_square(alist):
    Sum = 0
    for t in alist :
        Sum += t**2
    return Sum

exec(input().strip()) 