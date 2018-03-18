#locuri atacate
p1 = []
p2 = []

#harta cu avioane
av1 = []
av2 = []

#0 - loc gol
#1 - parte de avion
#2 - cap de avion
#3 - loc atacat
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    p1.append(row)
    p2.append(row)
    av1.append(row)
    av2.append(row)
del row
def smartPrint(m):
    sz = len(m)
    for i in range(sz):
        print(m[i])

smartPrint(p1)
print("\n")
smartPrint(p2)

def getCoord(s):
    if len(s)!=2 and len(s)!=3:
        raise ValueError
    else:
        return ord(s[0])-ord("A"),int(s[1])



turnCount=0
while True:
    turnCount += 1
    cont = input("Continue (type 'done' when you don't want to continue):")
    if cont=="done":
        break
    if turnCount%2==1:
        i = getCoord(input("P1's turn:"))
        ran,col = i[0],i[1]
        print(ran)
        print(col)
        smartPrint(p2)
        p2[ran][col]=2

    else:
        i = getCoord(input("P2's turn:"))
        ran,col = i[0],i[1]
        print(ran)
        print(col)
        smartPrint(p1)
        p1[ran][col]=2

p1[0][0] = 1
p2[0][0] = 7
smartPrint(p1)
print(p1)
print("\n")
smartPrint(p2)
print(p2)
print("\n")
smartPrint(av2)
print(av2)
print(av2[0][0])
print(p1==p2)
