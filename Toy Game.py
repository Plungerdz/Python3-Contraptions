
import random as 
import pprint
pp = pprint.PrettyPrinter()
n = 10
def star(x):
	return "*"
def row(x):
	global n
	return [star(i) for i in range(n)]
m = [row(i) for i in range(n)] #[["*","*","*"],["*","*","*"],["*","*","*"]]
#print(m)
pp.pprint(m)
indices=list(range(n))
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
#print(m)
print("\n")
pp.pprint(m)

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
	exec(c)
if (ni==i) and (nj==j):
	print("You've won")
else:
	print("You've lost")
