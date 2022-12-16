from statistics import mean
filename,year = input().split()
year = year[-2::]
grades = []
file = open(filename,"r")
for line in file :
    id,grade = line.split()
    if id[:2:] == year :
        grades.append(float(grade))
if len(grades) == 0 :
    print("No data")
else :
    print(min(grades),max(grades),mean(grades))