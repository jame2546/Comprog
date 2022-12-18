animaldict = {}
inp = input()
cnt = 0
data = []
while inp != "q" :
    name,animal = inp.split(",")[0].strip(),inp.split(",")[1].strip()
    if animal not in animaldict :
        animaldict[animal] = [name]
        data.append([cnt,animal])
        cnt += 1
    else :
        animaldict[animal].append(name)
    inp = input()
for t in data :
    print(t[1]+": "+", ".join(animaldict[t[1]]))