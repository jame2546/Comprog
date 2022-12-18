def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a,b,c) :
    return gcd(a,gcd(b,c)) == 1

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(1, max_len + 1) :
        for a in range(1, c) :
            for b in range(a, c):
                if a**2 + b**2 == c**2 and is_coprime(a, b, c):
                    triple.append([a, b, c])
    return triple

exec(input().strip())