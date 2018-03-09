import random as rn
m = [["*","*","*"],["*","*","*"],["*","*","*"]]
indices=list(range(2))
i = rn.choice(indices)
j = rn.choice(indices)
m[i][j]="@"
ni = rn.choice(indices)
while ni==i:
	ni = rn.choice(indices)
nj = rn.choice(indices)
while nj==j:
	nj = rn.choice(indices)
m[ni][nj]="#"
print(m)
def up():
	global ni
	ni+=1
def down():
	global ni
	ni-=1
def left():
	global nj
	nj+=1
def right():
	global nj
	nj-=1

code = input("Your code here:").split(";")
for c in code:
	eval(c)
if (ni==i) and (nj==j):
	print("You've won")
else:
	print("You've lost")
