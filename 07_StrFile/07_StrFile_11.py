word = input()
if word[-1] == "x" or word[-1] == "s" :
    print(word +"es")
elif word[-2::] == "ch" :
    print(word +"es")
elif word[-1] == 'y' and  word[-2] not in "aeiou":
    print(word[:-1:] + "ies")
else :
    print(word+'s')