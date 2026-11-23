import tkinter as tk
root =tk.Tk()
root.title("赤いbox消える")

canvas=tk.Canvas(root,width=600,height=500,bg="white")
canvas.pack()

x=20
y=100
box=canvas.create_rectangle(x,y,x+100,y+100,fill="red")

def delete_box(event):
    canvas.delete(box)
canvas.bind("<Button-1>",delete_box)

root.mainloop()