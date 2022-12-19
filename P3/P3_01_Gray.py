def builtbits(N) :
    codes = "0,1"   
    for i in range(int(N)-1) :
        codes = process(codes)
    return codes
    
def process(code) :
    code += ","+ ",".join(code.split(",")[::-1])
    code = code.split(",")
    for i in range(len(code)) :
        if i < len(code)/2 :
            code[i] = "0" + code[i]
        else :
            code[i] = "1" + code[i]
    return ",".join(code)
    
n = int(input())
k = int(input())
if n <= 0 and k < 1 :
    print("Invalid n and k")
elif n <= 0 :
    print("Invalid n")
elif k < 1 :
    print("Invalid k")
else :
    out = ""
    for i in range(1,k+1):
        m = n
        if i >= k :
            m -= 1
        if i >= 10 :
            m -= 1
        out += str(i) + '-'*m
    print(out)
    codes = builtbits(n) 
    outp = ""
    i = 0
    if len(codes) > len(out) :
        while i < len(codes) :
            outp += codes[i]
            i += 1
            if len(outp) == len(out) :
                print(outp)
                outp = ""
                i += 1
        if len(outp) != len(out) :
            print(outp)
    else :
        print(codes)