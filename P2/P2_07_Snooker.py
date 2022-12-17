Score = {'X':0, 'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7}
p1 = 0
p2 = 0
while True :
    inp = input()
    if inp[0] == "1" :
        for i in range(len(inp[1:])) :
            p1 += Score[inp[1:][i]]
    else :
        for i in range(len(inp[1:])) :
            p2 += Score[inp[1:][i]]
    if i == 0 and inp[1:][i] == "K" :
                break
print(p1,p2) 
if p1 > p2 :
    print("Player 1 wins")
elif p1 < p2 :
    print("Player 2 wins")
else :
    print("Tie")