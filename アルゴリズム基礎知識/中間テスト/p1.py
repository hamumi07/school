import tkinter as tk
import random

img=[None]*14
card=[0]*26
face=[0]*26

def draw_card():
    cvs.delete("all")
    for i in range(26):
        x=(i%8)*140+70
        y=int(i/8)*190+95
        if face[i]==0:
            cvs.create_image(x,y,image=img[0])
        if face[i]==1:
            cvs.create_image(x,y,image=img[card[i]])    

def shuffle_card():
    for i in range(26):
        card[i]=1+i%13
    for i in range(100):
        r1=random.randint(0,12)
        r2=random.randint(13,25) 
        card[r1],card[r2]=card[r2],card[r1]

def click(e):
    x=int(e.x/140)
    y=int(e.y/190)
    if 0<=x and x<=7 and 0<=y and y<=3:
        n=x+y*8
        if n >= 26:
            return
        if face[n]==0:
            face[n]=1
        else:
            face[n]=0 
        draw_card()     

root=tk.Tk()     
root.title("神経衰弱")   
root.resizable(False,False)
root.bind("<Button>",click)
cvs=tk.Canvas(width=1120,height=760,bg="#E2F8FD")
cvs.pack()
for i in range(14):
    img[i]=tk.PhotoImage(file="card/"+str(i)+".png")
shuffle_card()    
draw_card()
root.mainloop()