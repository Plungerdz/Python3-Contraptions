#from random import choice as ch
#from random import shuffle as sf

def randint(x):
    return int(round(random(1)*x))    

def ch(l):
    return l[randint(len(l)-1)]    

def sf(the_list):
    amnt_to_shuffle = len(the_list)
    while amnt_to_shuffle > 1:
        i = int(floor(random(1) * amnt_to_shuffle))
        amnt_to_shuffle -= 1
        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list

def toast(guess):
    s = ""
    for i in guess:
        s += i
    return s

def fbi(guess):
    global code
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

def out(s):
    global screenput
    screenput.append(s)

def keyPressed():
    global input, guess, turn, screenput, code, ok
    if key==BACKSPACE:
        input=input[:len(input)-1]
    elif key==ESC:
        exit()
    elif key==TAB:
        out(code)
    elif key==ENTER:
        guess=input
        input=""
        turn+=1
        output = fbs(fbi(guess))
        sf(output)
        output=toast(output)
        out(str(guess)+" "+str(output))
        if output == "AAAA":
            ok = True
        if turn==12 or ok:
            if ok:
                screenput= ["You've won!",code]
            else:
                screenput= ["You've lost!",code]
    elif key!=CODED:
        input+=key

def ltext(txt,x,y):
    global fontSize
    for i in range(len(txt)):
        text(txt[i],x,y+i*fontSize)
    
def setup():
    fullScreen()
    global f, input, guess, turn, screenput, fontSize, code, ok
    colors = ["R", "V", "P", "A", "G", "M"]
    code = ""
    for i in range(4):
        code += ch(colors)
    screenput=[]
    fontSize=48
    fill(0, 255, 0)
    f = loadFont("Consolas-48.vlw")
    input=""
    turn=0
    colors = ["R", "V", "P", "A", "G", "M"]
    code = ""
    for i in range(4):
        code += ch(colors)
    ok = False
    textFont(f,fontSize)
    
def draw():
    global input, screenput, fontSize
    background(0)
    ltext(screenput,fontSize,fontSize)
    text(input,width/2,height-fontSize)
