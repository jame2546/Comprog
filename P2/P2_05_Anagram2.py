def Format(word):
    return {c: word.lower().count(c) for c in sorted(word.lower()) if c in "abcdefghijklmnopqrstuvwxyz"}

def Addzero (word1,word2) :
    for t in word1 :
        if t not in word2 :
            word2[t] = 0
    for t in word2 :
        if t not in word1 :
            word1[t] = 0
    
def Process(word1,word2) :
    word1,word2 = Format(word1),Format(word2)
    Addzero(word1,word2)
    del_1 = []
    del_2 = []
    for t in word1 :
        while word1[t] > word2[t] :
            word1[t] -= 1
            del_1.append(t)
    for t in word2 :
        while word2[t] > word1[t] :
            word2[t] -= 1
            del_2.append(t)
    return sorted(del_1),sorted(del_2)

def Count(list) :
    ret = {}
    for c in list :
        if c in ret :
            ret[c] += 1
        else :
            ret[c] = 1
    return ret

def Output(dict,head) :
    print(head)
    if len(dict) == 0 :
        print(" - None")
    else :
        for t in sorted(dict) :
            if dict[t] == 1 :
                print(" - remove 1",t)
            else :
                print(" - remove",str(dict[t]),t+"'s")

word1 = input()
word2 = input()
del_1,del_2 = Process(word1,word2)
Output(Count(del_1),word1)
Output(Count(del_2),word2)

