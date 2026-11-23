import tkinter as tk
img=[None]*14
def draw_card():
    for i in range(14):
        x=(i%7)*120+60
        y=int(i/7)*168+84
        cvs.create_image(x,y,image=img[i])

root=tk.Tk()     
root.title("神経衰弱")   
root.resizable(False,False)
cvs=tk.Canvas(width=960,height=672)
cvs.pack()
for i in range(14):
    img[i]=tk.PhotoImage(file="card/"+str(i)+".png")
draw_card()
root.mainloop()