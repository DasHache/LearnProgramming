import Tkinter as Tk
from world import World

class Game:
    def __init__(self):
        print "I am a constructor of the class Game"

game = Game()        
world = World()
a = Tk.Tk()
canvas = Tk.Canvas(a, width=300, height=200)
canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
canvas.pack()
a.mainloop()
 
