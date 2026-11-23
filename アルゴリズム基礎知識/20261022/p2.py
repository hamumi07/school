import tkinter as tk
x=30
y=100
xp=5
def animation():
    global x,xp
    x=x+xp
    if x>=360: xp=-5
    if x<=0: xp=-5
    cvs.delete("all")
    cvs.create_rectangle(x,y,x+40,y+40,fill="red",width=0)
    root.after(50,animation)
root=tk.Tk()
root.geometry("400x200")
cvs=tk.Canvas(root,width=400,height=200,bg="white")
cvs.pack()
animation()
root.mainloop()