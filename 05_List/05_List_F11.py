def missing_digits(s):
    numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for t in s :
        if t in numbers :
            numbers.remove(t)
    if numbers == [] :
        return "None"
    else :
        return [int(e) for e in numbers]
exec(input()) # DON'T remove this line