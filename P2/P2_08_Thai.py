num = {'0':'soon','1':'neung','2':'song','3':'sam','4':'si',
      '5':'ha','6':'hok','7':'chet','8':'paet','9':'kao'}
def to_Thai( N ):
    out = []
    if N >= 1000: 
        out.append(num[str(N)[0]])
        out.append("pun")
        N %= 1000
    if N >= 100: 
        out.append(num[str(N)[0]])  
        out.append("roi")
        N %= 100
    if N >= 10:
        last = N//10
        if last == 2 :
            out.append("yi")
        elif last != 1 :
            out.append(num[str(N)[0]])
        out.append("sip")
        N %= 10
    if N == 0 :
        if out == [] :
            return "soon"
        return " ".join(out)
    if len(out) > 0 and N == 1 :
        out.append("et")
    else :
        out.append(num[str(N)[0]])
    return " ".join(out)
exec(input().strip())