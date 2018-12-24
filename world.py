import Tkinter as Tk
class World:
    def __init__(self):
        print "I am a constructor of the class World"
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=300, height=200)
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100,  fill="black")
        canvas.create_rectangle(50, 120, 100, 80,  fill="red")
        canvas.create_rectangle(80, 100, 150, 100,  fill="brown")
        canvas.pack()

    def run(self):
        self.a.mainloop()

