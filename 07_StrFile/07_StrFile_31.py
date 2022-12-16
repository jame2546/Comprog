def R (DNA) :
    pairs = {"A":"T","T":"A","G":"C","C":"G"}
    res = ""
    for t in DNA[::-1] :
        res += pairs[t]
    return res

def F (DNA) :
    Npairs = {"A":0,"T":0,"G":0,"C":0}
    for t in DNA :
        Npairs[t] += 1
    return "A="+str(Npairs["A"])+", "+"T="+str(Npairs["T"])+", ""G="+str(Npairs["G"])+", ""C="+str(Npairs["C"])

def D (DNA) :
    find = input()
    cnt = 0
    for i in range(len(DNA)-1) :
        if DNA[i:i+2] == find :
            cnt += 1
    return cnt

def CheckDNA (DNA) :
    for t in DNA :
        if t not in "ATGC" :
            return False
    return True

DNA = input().strip().upper()
cmd = input()
if CheckDNA(DNA) :
    if cmd == "R" :
        print(R(DNA))
    elif cmd == "F" :
        print(F(DNA)) 
    elif cmd == "D" :
        print(D(DNA))
else :
    print("Invalid DNA")