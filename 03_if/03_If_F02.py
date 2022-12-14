def choose(stu1, stu2):
    id_1,gpa_1,comp_1,cal1_1,cal2_1 = stu1[0],stu1[1],stu1[2],stu1[3],stu1[4]
    id_2,gpa_2,comp_2,cal1_2,cal2_2 = stu2[0],stu2[1],stu2[2],stu2[3],stu2[4]
    person1 = True
    person2 = True
    if comp_1 != "A" or cal1_1 > "C" or cal2_1 > "C" :
        person1 = False
    if comp_2 != "A" or cal1_2 > "C" or cal2_2 > "C" :
        person2 = False
    if person1 == False and person2 == False :
        return []
    if person1 == True and person2 == False :
        return [id_1]
    if person1 == False and person2 == True :
        return [id_2]
    if person1 == True and person2 == True :
        if gpa_1 > gpa_2 :
            return [id_1]
        if gpa_2 > gpa_1 :
            return [id_2]
        if gpa_1 == gpa_2 :
            if cal1_1 < cal1_2 :
                return [id_1]
            if cal1_2 < cal1_1 :
                return [id_2]
            if cal1_1 == cal1_2 :
                if cal2_1 < cal2_2 :
                    return [id_1]
                if cal2_2 < cal2_1 :
                    return [id_2]
                if cal2_1 == cal2_2 :
                    return [id_1,id_2]
exec(input()) # DON'T remove this line