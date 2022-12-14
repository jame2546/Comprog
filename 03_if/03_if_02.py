id1,gpa1,com1,cal11,cal21 = input().split()
id2,gpa2,com2,cal12,cal22 = input().split()
person1 = True
person2 = True
while person1 != False and person2 != False :
    if com1 != "A" or cal11 > "C" or cal21 > "C" :
        person1 = False
    if com2 != "A" or cal12 > "C" or cal22 > "C" :
        person2 = False 
    if person1 == True and person2 == False :
        print(id1)
        break
    elif person1 == False and person2 == True :
        print(id2)
        break
    if person1 == False and person2 == False :
        print("None")
        break
    if float(gpa1) > float(gpa2):
        print(id1)
        break
    elif float(gpa1) < float(gpa2):
        print(id2)
        break
    elif float(gpa1) == float(gpa2) :
        if [cal11,cal21] > [cal12,cal22] :
            print(id2)
            break
        elif [cal11,cal21] < [cal12,cal22] :
            print(id1)
            break
        elif [cal11,cal21] == [cal12,cal22] :
            print("Both")
            break