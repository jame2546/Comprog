def change_grade(grade):
    upgrades = ["A", "A", "B+", "B", "C+", "C", "D+", "D", "D"]
    return upgrades[["A", "B+", "B", "C+", "C", "D+", "D", "F"].index(grade)]

def index_of(grades, ID):
    for i, (id, grade) in enumerate(grades):
        if id == ID:
            return i
    return -1

def upgrade(grades, IDs):
    for ID in IDs:
        index = index_of(grades, ID)
        if index != -1:
            grades[index][1] = change_grade(grades[index][1])
    grades.sort()

exec(input())
exec(input())
exec(input())