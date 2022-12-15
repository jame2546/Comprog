def Upgrade(grade) :
    grades = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
    if grade == "A" :
        return "A"
    else :
        return grades[grades.index(grade) + 1]
list = []
inp = input()
while inp != "q" :
    id,grade = inp.split()
    list.append([id,grade])
    inp = input()
list.sort()
uids = input().split()
for t in list :
    if t[0] in uids :
        print(t[0],Upgrade(t[1]))
    else :
        print(t[0],t[1])
