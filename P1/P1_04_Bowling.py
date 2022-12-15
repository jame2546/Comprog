def getFrame(res) :
    score_frame = [""]*10
    curr_frame = 0
    i = 0
    while True :
        if curr_frame != 9 :
            if res[i] == "X" :
                score_frame[curr_frame] += res[i] + res[i+1] + res[i+2]
                curr_frame += 1
            elif res[i] != "X" and res[i] != "/" :
                score_frame[curr_frame] += res[i] + res[i+1]
                if res[i+1] == "/" :
                    score_frame[curr_frame] += res[i+2]
                else :
                    i += 1
                curr_frame += 1 
            i += 1
        else :
            if res[i] == "X" :
                score_frame[curr_frame] += res[i] + res[i+1] + res[i+2]
                break
            elif res[i] != "X" and res[i] != "/" :
                score_frame[curr_frame] += res[i] + res[i+1]
                if res[i+1] == "/" :
                    score_frame[curr_frame] += res[i+2]
                break
            i += 1
    return score_frame
        
def Calscore(char) :
    score = 0
    for i in range(len(char)) :
        if char[i] == "X" :
            score += 10
        elif char[i] == "/" :
            score += 10-int(char[i-1])
        else :
            score += int(char[i])
    return score

def getScore(frame) :
    Score = []
    for i in range(len(frame)) :
        Score.append(int(Calscore(frame[i])))  
    return Score


res = input()
Score = getScore(getFrame(res))
frame = int(input())
if frame in [1,2,3,4,5,6,7,8,9,10] :
    print(Score[frame-1])
else :
    print(sum(Score))