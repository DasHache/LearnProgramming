import Tkinter as Tk
# from timer import InfiniteLoopTimer
from tank import Tank
from time import sleep

class World():

    def __init__(self, game):
        print "I am a constructor of the class World"
        self.game = game
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=600, height=500)
        self.canvas = canvas
        canvas.create_rectangle(20, 30, 575, 460, fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100, fill="black")
        canvas.pack()

        self.update_period = 1000 # ms
        self.recalc_period = 500 # ms

        # DEBUG information. Will be removed later.
        self.mark_update = None
        self.mark_recalc = None

    def run(self):
        self.addTank()
        self.update() # infinite loop for Update!
        self.recalc() # infinite loop for Re-calc!
        self.a.mainloop()

    def addTank(self):
        self.t = Tank(self, 70, 100)
        self.t.draw()

    def update(self):
        self.__mark_update()
        if self.game.running:
            self.canvas.after(self.update_period, self.update)
        else:
            self.a.quit() # quit the mainloop

    def recalc(self):
        self.__mark_recalc()
        if self.game.running:
            self.canvas.after(self.recalc_period, self.recalc)
        else:
            self.a.quit() # quit the mainloop

    def __mark_update(self):
        print "U-"
        if self.mark_update:
            self.canvas.delete(self.mark_update)
            self.mark_update = None
        else:
            self.mark_update = self.canvas.create_oval(25, 5, 45, 25, fill="red")

    def __mark_recalc(self):
        print "-R"
        if self.mark_recalc: 
            self.canvas.delete(self.mark_recalc)
            self.mark_recalc = None
        else:
            self.mark_recalc = self.canvas.create_oval(55, 5, 75, 25, fill="green")


