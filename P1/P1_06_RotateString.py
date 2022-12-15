def Checksize (word) :
    for i in range(1,len(word)) :
        if len(word[i-1]) != len(word[i]) :
            return False
    return True

def Getinput(n) :
    word = []
    for i in range(n) :
        word.append(input())
    return word

def halfpi (word) :
    res = [""]*len(word[0])
    for i in range(len(word[0])) :
        for j in range(len(word)) :
            res[i] += word[j][i]
        res[i] = res[i][::-1]
    return "\n".join(res)

def flip (word) :
    res = []
    for t in word :
        res.append(t[::-1])
    return "\n".join(res)
def pi (word) :
    return flip(word[::-1])

oper = input()
word = Getinput(int(input()))
if Checksize(word) == True :
    if oper == "90" :
        print(halfpi(word))
    elif oper == "180" :
        print(pi(word))
    elif oper == "flip" :
        print(flip(word))
else :
    print("Invalid size")