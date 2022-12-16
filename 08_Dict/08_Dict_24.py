alphabets = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def text2keys( text ):
    key = []
    text = "".join([e for e in text.lower() if e in "abcdefghijklmnopqrstuvwxyz "])
    for t in text :
        if t == " " :
            key.append("0")
        else :
            for i in range(len(alphabets)) :
                if t in alphabets[i] :
                    for j in range(len(alphabets[i])) :
                        if t == alphabets[i][j] :
                            key.append(str(i+2)*(j+1))
    return " ".join(key)

def keys2text( keys ):
    txt = ""
    for t  in keys.split() :
        if t != "0" :
            i = int(t[0]) - 2
            j = len(t) - 1
            txt += alphabets[i][j]
        else :
            txt += " "
    return txt

exec(input().strip())