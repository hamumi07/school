import tkinter as tk
import random

img=[None]*14
card=[0]*26
face=[0]*26
proc=0
tmr=0
se11=0
se12=0
you=0
com=0
FNT=("Times New Roman",36)

def draw_card():
    cvs.delete("all")
    for i in range(26):
        x=(i%7)*120+60
        y=int(i/7)*168+84
        if face[i]==0:
            cvs.create_image(x,y,image=img[0])
        if face[i]==1:
            cvs.create_image(x,y,image=img[card[i]])    

def shuffle_card():
    for i in range(26):
        card[i]=1+i%13
        face[i]=0
    for i in range(100):
        r1=random.randint(0,12)
        r2=random.randint(13,25) 
        card[r1],card[r2]=card[r2],card[r1]

def click(e):
    global proc,tmr,se11,se12,you,com
    if proc==0:
        shuffle_card()
        you=0
        com=0
        proc=1
        return
    x=int(e.x/120)
    y=int(e.y/168)
    if 0<=x and x<=6 and 0<=y and y<=3:
        n=x+y*7
        if n >= 26:
            return
        if face[n]==0:
            if proc==1:
                face[n] =1
                se11=n
                proc=2
            elif proc==2:
                face[n] =1
                se12=n
                proc=3
                tmr=0

def main():
    global proc,tmr,se11,se12,you,com
    tmr +=1
    draw_card()
    if proc==0 and tmr%10<5: #スタート待ち
            cvs.create_text(780,580,text="Click to start",fill="green",font=FNT)
    if 1<=proc and proc<=3:
        cvs.create_rectangle(840,60,960,200,fill="blue",width=0) 
        cvs.create_text(900,100,text="You",fill="silver",font=FNT)
        cvs.create_text(900,160,text=you,fill="white",font=FNT)
    if 4<=proc and proc<=6:
        cvs.create_rectangle(840,260,960,400,fill="red",width=0) 
        cvs.create_text(900,300,text="COM",fill="silver",font=FNT)
        cvs.create_text(900,360,text=com,fill="white",font=FNT)
    if proc==3 and tmr==15:#揃ったか判定
        if card[se11]==card[se12]:
            face[se11]=2
            face[se12]=2
            you += 2
            proc=1
            if you+com==26: proc=7
        else:
            face[se11]=0
            face[se12]=0
            proc=4
        tmr=0
    if proc==4 and tmr==5: #COM 1枚目をめくる
        se11=random.randint(0,25)
        while face[se11]!=0: se11=(se11+1)%26
        face[se11]=1
        proc=5
        tmr=0
    if proc==5 and tmr==5: #COM 2枚目をめくる
        se12=random.randint(0,25)
        while face[se12]!=0: se12=(se12+1)%26
        face[se12]=1
        proc=6
        tmr=0
    if proc==6 and tmr==15:#揃ったか判定
        if card[se11]==card[se12]:
            face[se11]=2
            face[se12]=2
            com+=2
            proc=4
            if you+com==26: proc=7
        else:
            face[se11]=0
            face[se12]=0
            proc=1
        tmr=0
    if proc==7:
        if you>com:
            cvs.create_text(780,580,text="You WIN!",fill="skyblue",font=FNT)
        if com>you:
            cvs.create_text(780,580,text="COM WIN!",fill="pink",font=FNT) 
        if tmr==25:
            proc=0       
    root.after(200,main)        

root=tk.Tk()     
root.title("神経衰弱")   
root.resizable(False,False)
root.bind("<Button>",click)
cvs=tk.Canvas(width=960,height=672,bg="black")
cvs.pack()
for i in range(14):
    img[i]=tk.PhotoImage(file="card/"+str(i)+".png")
main()
root.mainloop()