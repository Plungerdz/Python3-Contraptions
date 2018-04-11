from random import choice as ch
from random import shuffle as sf

colors = ["R", "V", "P", "A", "G", "M"]
code = ""
for i in range(4):
    code += ch(colors)

ok = False

def toast(guess):
    s = ""
    for i in guess:
        s += i
    return s

def fbi(guess):
    l = [i for i in code]
    aux=[i for i in guess]
    for i in range(len(l)):
        part="_"
        if aux[i]==l[i]:
            part="A"
            l[i]="*"
            aux[i]="*"
        yield part
    yield l
    yield guess

def fbs(fbi):
    fbi=list(fbi)
    ln=len(fbi)
    t=fbi[:ln-2]
    l=fbi[ln-2]
    guess=fbi[ln-1]
    for i in range(len(l)):
        if (guess[i] in l) and (t[i]!="A"):
            l[i]="*"
            t[i]="N"
    return t

for i in range(12):
    guess = input("your guess here:")
    output = fbs(fbi(guess))
    sf(output)
    output=toast(output)
    print(guess, " ", output)
    if output == "AAAA":
        ok = True
        break

if ok:
    print("You've won!")
else:
    print("You've lost!")
