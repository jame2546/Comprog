def number_name(n):
    n = int(n)
    digit = [0,1,2,3,4,5,6,7,8,9]
    eng = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    p = eng[digit.index(n)]
    return p
exec(input()) # DON'T remove this line