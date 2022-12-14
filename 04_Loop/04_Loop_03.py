ans = input()
sol = input()
if len(ans) != len(sol) :
    print("Incomplete answer")
else :
    score = 0
    for i in range(len(ans)) :
        if ans[i] == sol[i] :
                score += 1
    print(score)