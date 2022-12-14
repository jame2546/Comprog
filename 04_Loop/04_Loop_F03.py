def grade_mcq(sol, ans):    
    if len(ans) != len(sol):
        return -1 
    else:
        n = 0
        for i in range(len(ans)) :
            if ans[i] == sol[i] :
                n += 1
        return n
exec(input()) # DON'T remove this line