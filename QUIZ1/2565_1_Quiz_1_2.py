def f1(a, b, c):
    sets = [[a], [b], [c], [a, b], [b, c], [a, c], [a, b, c]]
    tmp = []
    for t in sets:
        if min(t) > 0:
            tmp.append(min(t))
    return min(tmp)
    ##### other way ######
    


def f2(a, b, c):
    sets = [[a], [b], [c], [a, b], [b, c], [a, c], [a, b, c]]
    tmp = []
    for t in sets:
        if max(t) < 0:
            tmp.append(min(t))
    return max(tmp)


def f3(a, b, c):
    return str(abs(sum([a, b, c])))[0]


def f4(a, b, c):
    return str(abs(sum([a, b, c])))[-1]


def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a, b, c))
    elif s1 == 0 and s2 == 1:
        print(f2(a, b, c))
    elif s1 == 1 and s2 == 0:
        print(f3(a, b, c))
    elif s1 == 1 and s2 == 1:
        print(f4(a, b, c))
    else:
        print("Error")


exec(input())
