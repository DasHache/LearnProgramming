import Tkinter as Tk
class World:
    def __init__(self):
        print "I am a constructor of the class World"
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=300, height=200)
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.pack()

    def run(self):
        self.a.mainloop()

