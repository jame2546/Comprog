def readColor(filename) :
    colors = []
    file = open(filename,"r")
    for line in file :
        line = line.strip().split()
        for color in line :
            colors.append(color.lower())
    return colors

def fixLyric(filename) :
    file = open(filename,"r")
    for line in file :
        line = line.strip().split(" ")
        for i in range(len(line)) :
            line[i] = addColor(line[i])
        print(" ".join(line))


def addColor(word) :
    for t in colors :
        run = False
        for i in range(len(word)) :
            for j in range(i,len(word)) :
                if word[i:j+1].lower() == t :
                    word = "<"+t+">"+word[i:j+1]+"</>" + word[j+1:]
                    run = True
                    if run :
                        break
            if run :
                break
    return word

colors = readColor(input())
fixLyric(input())
