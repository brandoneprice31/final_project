from Tkinter import *

def callback():
    print "called the callback!"

root = Tk()

root.title('Tic Tac Toe')
root.geometry('500x500')

cw = 500
ch = 500
w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()

for i in range(1,3):
    w.create_rectangle(i*cw/3-1,0,i*cw/3-1,ch, fill="black")

for i in range(1,3):
    w.create_rectangle(0,i*cw/3-1,cw,i*cw/3-1, fill="black")

mainloop()