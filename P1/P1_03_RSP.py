m = int(input())  
score1 = 0
score2 = 0
times = 0

outcomes = {
    ("R", "P"): 2,  # Player 2 wins
    ("R", "S"): 1,  # Player 1 wins
    ("P", "R"): 1,  # Player 1 wins
    ("P", "S"): 2,  # Player 2 wins
    ("S", "R"): 2,  # Player 2 wins
    ("S", "P"): 1,  # Player 1 wins
}

while score1 < m and score2 < m and times < 3*m:
    hand1, hand2 = input().split()
    if hand1 == hand2:
        pass
    else:
        outcome = outcomes[(hand1, hand2)]
        if outcome == 1:
            score1 += 1
        elif outcome == 2:
            score2 += 1
    times += 1

print(score1, score2)

if times == 3*m and score1 == score2 :
    print("Tie")
elif score1 > score2:
    print("Player 1 wins")
elif score2 > score1:
    print("Player 2 wins")
