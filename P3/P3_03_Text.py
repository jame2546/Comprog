fname = "data1.txt"
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1) 
if k - len(ruler) >= 0 :
    ruler += '-'*( k - len(ruler) ) 
print(ruler)
txt = ""
with open(fname,"r") as file :
    for line in file :
        txt += line.replace("\n",".")

