def Cut(cards):
    lst = cards.split()
    n = len(lst) // 2
    lst = lst[n:] + lst[:n]
    return " ".join(lst)

def Shuffle(cards):
    cl = cards.split()
    sl = []
    for i in range(len(cl)):
        if i % 2 == 0:
            sl.append(cl[i // 2])
        else:
            sl.append(cl[len(cl) // 2 + i // 2])
    return " ".join(sl)

cards = input()
cmd = input()
for t in cmd :
    if t == "C" :
        cards = Cut(cards)
    elif t == "S" :
        cards = Shuffle(cards)
print(cards)