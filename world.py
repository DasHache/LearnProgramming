class World:
    def __init__(self):
        import Tkinter as Tk
        print "I am a constructor of the class World"
        a = Tk.Tk()
        canvas = Tk.Canvas(a, width=300, height=200)
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.pack()

    def run(self):
        a.mainloop()

w = World()
