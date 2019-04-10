import Tkinter as Tk
from timer import InfiniteLoopTimer
from tank import Tank

class World:
    def __init__(self):
        print "I am a constructor of the class World"
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=600, height=500)
        self.canvas = canvas
        canvas.create_rectangle(20, 20, 560, 460, fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100, fill="black")
        canvas.pack()
        
    def run(self):

        # create a timer for the World re-Draw (update)
        self.timerUpdate = InfiniteLoopTimer(self, self, "update")
        # start the timer
        self.timerUpdate.start()
        
        self.addTank()
        self.a.mainloop()

    def addTank(self):
        self.t = Tank(self, 70, 100)
        self.t.draw()

    def update(self):
        ''' Function to update the world (re-draw it)
        '''
        print "World.update() was called!"
