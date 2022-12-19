def lstScore(target) :
    lst = []
    for file,doc in Dictfile.items() :
        temp = []
        doc = doc.split()
        all_word = len(doc)
        cnt = 0
        for word in doc :
            if word == target :
                cnt += 1
            if word not in temp :
                temp.append(word)
        score = (cnt/all_word)*(1/len(temp))
        lst.append([-score,file])
    lst.sort()
    return lst

n = int(input())
Dictfile = {}
for i in range(n) :
    file = input()
    doc = input()
    Dictfile[file] = doc
target = input()
while target != "-1" :
    a = lstScore(target) 
    if a[0][0] != 0 :
        print(a[0][1])
    else :
        print("NOT FOUND")
    target = input()