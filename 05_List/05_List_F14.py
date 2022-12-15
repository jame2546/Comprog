def peaks(x):
    x = [float(e) for e in x]
    n = []
    for i in range(len(x)-2) :
        if x[i] < x[i+1] and x[i+1] > x[i+2] :
            n.append(i+1) 
    return n
exec(input()) # DON'T remove this line