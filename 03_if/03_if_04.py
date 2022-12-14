num = input()
if len(num) == 10 and (num[:2] == "06" or num[:2] == "08" or num[:2] == "09" )  :
    print("Mobile number")
else :
    print("Not a mobile number")