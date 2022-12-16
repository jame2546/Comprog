def no_lowercase(t): 
    return t == t.upper()

def no_uppercase(t):
    return t == t.lower()

def no_number(t):
    for char in t :
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
            return False
    return True

def no_symbol(t):
    for char in t :
        if char in [",",".","\'","\"","(",")","[","]","<",">","!","@","#","$","%","^","&","*","-","+"] :
            return False
    return True
    
def character_repetition(password): 
    cnt = 1
    for i in range(1,len(password)) :
        if password[i-1] == password[i] :
            cnt += 1
            if cnt == 4 :
                return True
        else :
            cnt = 1
        
def number_sequence(password): 
    num = "01234567890"
    for i in range(len(num)-3) :
        if num[i:i+4:] in password or num[i:i+4:][::-1] in password :
            return True   

def letter_sequence(password): 
    let = "abcdefghijklmnopqrstuvwxyza"
    for i in range(len(let)-3) :
        if let[i:i+4:] in password.lower() or let[i:i+4:][::-1] in password.lower() :
            return True

def keyboard_pattern(password): 
    key = "!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(len(key)-3) :
        if key[i:i+4:].lower() in password.lower() or key[i:i+4:][::-1].lower() in password.lower() :
            return True

password = input().strip()
errors = []
if len(password) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(password) == True : 
    errors.append("No lowercase letters")
if no_uppercase(password) == True :
    errors.append("No uppercase letters")
if no_number(password) == True :
    errors.append("No numbers")
if no_symbol(password) == True :
    errors.append("No symbols")
if character_repetition(password) == True :
    errors.append("Character repetition")
if number_sequence(password) == True :
    errors.append("Number sequence")
if letter_sequence(password) == True :
    errors.append("Letter sequence")
if keyboard_pattern(password) == True :
    errors.append("Keyboard pattern")
if len(errors) == 0: 
    print("OK")
else: 
    print("\n".join(errors))