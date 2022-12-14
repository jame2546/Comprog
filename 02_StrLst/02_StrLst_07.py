def Decryp (code) :
    Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp =  str(int(code[3::7])+int(code[7::5])+10000)[-4:-1]
    res = temp
    temp = Alphabets[int(str(int(temp[0]) + int(temp[1]) + int(temp[2]))[-1]) ].upper()
    return res + temp
print(Decryp(input()))