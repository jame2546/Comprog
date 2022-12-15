def Upgrade(grade) :
    grades = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
    if grade == "A" :
        return "A"
    else :
        return grades[grades.index(grade) + 1]
inp = input()
ids = []
grades = []
while inp != "q" :
    id,grade = input().split()
    ids.append(id)
    grades.append(grade)
    inp = input()
    