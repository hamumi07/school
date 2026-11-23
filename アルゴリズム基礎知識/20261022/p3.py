import tkinter as tk
def on_click(event):
    item_id=canvas.find_withtag("current")
    canvas.delete(item_id)
root=tk.Tk()

canvas=tk.Canvas(root,width=600,height=500,bg="white")
canvas.pack()
x = 20
y = 100
box = canvas.create_rectangle(x, y, x + 60, y + 60, fill="red")

def move_box():
    global x
    x = x + 5 
    canvas.coords(box, x, y, x + 60, y + 60)
    root.after(30, move_box)

canvas.tag_bind(box,"<Button-1>",on_click)    

move_box()
root.mainloop()