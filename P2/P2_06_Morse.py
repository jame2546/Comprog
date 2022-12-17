def getMorse(pattern,text) :
    morse = ''
    for e in text :
        j = pattern.find('[' + e + ']')
        if j == -1 :
            return "Invalid : "+text
        j += 3
        k = pattern.find('[',j)
        morse += pattern[j:k] + ' '
    return morse.strip()

def getText(pattern,morse) :
    text = ""
    for t in morse.split() :
        j = pattern.find(']' + t + '[')
        if j == -1 :
            return "Invalid : "+morse
        text += pattern[j-1]
    return text

with open(input(),"r") as file :
    op = file.readline().strip()
    pattern = file.readline().strip()
    if op not in ["T2M","M2T"] :
        print("Invalid code")
    else :
        for line in file :
            line = line.strip()
            if op == "T2M" :
                print(getMorse(pattern,line))
            elif op == "M2T" :        
                print(getText(pattern,line))
               
