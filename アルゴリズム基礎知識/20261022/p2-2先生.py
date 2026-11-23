import tkinter as tk
root=tk.Tk()

root.title("練習2-move()を使うやり方")
root.geometry("600x600")

canvas=tk.Canvas(root,width=600,height=600,bg="white")
canvas.pack()

box=canvas.create_rectangle(20,100,80,160,fill="red")

def move_box():
    canvas.move(box,5,0)
    root.after(30,move_box)
move_box()
root.mainloop()