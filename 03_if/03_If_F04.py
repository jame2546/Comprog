def is_mobile_number(number) :
    if len(number) == 10 and (number[0:2] == "06" or number[0:2] == "08" or number[0:2] == "09") :
        return True
    return False
exec(input()) # DON'T remove this line