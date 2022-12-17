def diffValue (c1,c2) :
    values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'C':1,'D':2,'H':3,'S':4}
    if c1[0] != c2[0] :
        if values[c1[0]] - values[c2[0]] > 0 :
            return "+"+str(values[c1[0]] - values[c2[0]])
        return str(values[c1[0]] - values[c2[0]])
    else :
        if values[c1[1]] - values[c2[1]] > 0 :
            return "+"+str(values[c1[1]] - values[c2[1]])
        return str(values[c1[1]] - values[c2[1]])
Card = input().upper().strip()
Card = [Card[i:i+2] for i in range(0, len(Card), 2)]
res = ""
for i in range(1,len(Card)) :
    res += diffValue(Card[i-1],Card[i])
print(res)