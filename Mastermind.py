from random import choice as ch
colors = ["R", "V", "P", "A", "G","M"]
code = ""
for i in range(4):
	code+=ch(colors)
code="RRPM"

ok=False

def fb(guess):
	l=[i for i in code]
	print("l: ",l)
	for i in range(len(guess)):
		part="_"
		if guess[i] in l:
			part="N"
		if guess[i]==code[i]:
			part="A"
		l[i]="*"
		yield part

def toast(guess):
	s=""
	for i in guess:
		s+=i
	return s
		
for i in range(12):
	guess=input("your guess here:")
	output=toast(list(fb(guess)))
	print(guess, " ", output)
	if output=="AAAA":
		ok=True
		break

if ok:
	print("You've won!")
else:
	print("You've lost!")
	
