numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
for t in input() :
    if t in numbers :
        numbers.remove(t)
if numbers == [] :
    print("None")
else :
    print(",".join(numbers))