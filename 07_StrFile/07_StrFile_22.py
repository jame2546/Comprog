def nospace (s) :
    outp = ""
    for t in s :
        if t != " " :
            outp += t
    return outp
sentence = nospace(input())
check = nospace(input())
if sorted(sentence.lower()) == sorted(check.lower()) :
    print("YES")
else :
    print("NO")