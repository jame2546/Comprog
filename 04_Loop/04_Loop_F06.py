def print_triangle(h):
    for i in range(h-1) :
        if i == 0 :
            print("."*(h-1) + "*" )
        elif  i == 1 :
            print("."*(h-i-1) + "*" + "."*i + "*")
        elif i != h - 1 :
            print("."*(h-i-1) + "*" + "."*(2*i-1) + "*")
    print("*"*(2*h-1))

        
exec(input()) # DON'T remove this line