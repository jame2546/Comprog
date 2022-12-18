def min(sec):
    min = sec // 60
    rem = sec % 60
    if rem < 10:
        return str(min) + ":0" + str(rem)
    else:
        return str(min) + ":" + str(rem)

def sec (time) :
    min,sec = time.split(":")
    return int(min)*60+int(sec)

Times = {}
for i in range(int(input())) :
    inp = input().split(",")
    genre,time = inp[-2].strip(),inp[-1]
    if genre in Times :
        Times[genre] += sec(time)
    else :
        Times[genre] = sec(time)
rev_Times = {v:k for k,v in Times.items()}
for t in sorted(Times.values(),reverse=True)[:3] :
    print(rev_Times[t]+" --> "+min(t))