import Tkinter as Tk
from threading import Timer


class World:
    def __init__(self):
        print "I am a constructor of the class World"
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=300, height=200)
        self.canvas = canvas
        self.x = 150
        self.x1 = 130
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100,  fill="black")
        canvas.pack()
        
        
    def run(self):
        self.a.mainloop()

