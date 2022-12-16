sentence = input()
outp = ""
a = ""
for t in sentence :
    if t not in "/,<>\'\"()[]-+.;:" :
        outp += t
    else :
        outp += " "
for i in range(len(outp.split())) :
    if i == 0 :
        a += outp.split()[i].lower()
    else :
        a += outp.split()[i][0].upper() + outp.split()[i][1::].lower()
print(a)