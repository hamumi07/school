import tkinter as tk

root=tk.Tk()
root.title("練習問題3-クリックしたらBoxを消す")

canvas=tk.Canvas(root,width=600,height=500,bg="white")
canvas.pack()

x=20
y=100
box=canvas.create_rectangle(x,y,x+60,y+60,fill="red")

def move_box():
    global x
    x=x+5
    canvas.coords(box,x,y,x+60,y+60)
    root.after(30,move_box)

def delete_box(event):
    canvas.delete(box)

canvas.tag_bind(box,"<Button-1>",delete_box)    
    
move_box()
root.mainloop()