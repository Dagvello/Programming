"""Урок Первый"""
from tkinter import *


root = Tk()
class grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        c.create_arc(self.x + i, 165, self.y + i, 235, start=180, extent=-90, style=ARC, outline='green', width=2)

c = Canvas(width=200, height=200, bg='white')
c.pack()
c.create_line(100, 180, 100, 50, fill='lightblue', width=90, arrow=LAST, arrowshape="50 50 20")
c.create_oval(150,5,190,45, fill='orange',outline='orange')

for i in range(0,200,10 ):
    grass(0,30)

root.mainloop()
