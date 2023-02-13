def calScore(word) :
    table = ["","AEILNORSTU","DG","BCMP","FHVWY","K","","","JX","","QZ"]
    score = 0
    for char in word :
        for i in range(len(table)) :
            if char in table[i] :
                score += i 
    return score

words = input().split() 
score = []
for word in words :
    score.append([calScore(word),word])
for t in sorted(score,reverse=True) :
    print(t[1],t[0])