import Tkinter as Tk
from timer import InfiniteLoopTimer
from tank import Tank
from time import sleep

class World():

    def __init__(self, game):
        print "I am a constructor of the class World"
        self.game = game
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=600, height=500)
        self.canvas = canvas
        canvas.create_rectangle(20, 20, 560, 460, fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100, fill="black")
        canvas.pack()

    def run(self):
        # create a timer for the World re-Draw (what you SEE)
        self.timerUpdate = InfiniteLoopTimer(self, self, "update")
        # start the timer
        self.timerUpdate.start()

        # create a timer for the World re-Calculation (what really is)
        self.timerRecalc = InfiniteLoopTimer(self, self, "recalc")
        # start the timer
        self.timerRecalc.start()
        
        self.addTank()

        # self.a.protocol("WM_DELETE_WINDOW", self.__on_close)

        print "MAINLOOOOP"
        self.a.mainloop()

    def stop_mainloop(self):

        self.a.quit()

        print "joining-U"
        self.timerUpdate.t.join()
        print "joining-U = DONE!"

        print "joining-R"
        self.timerRecalc.t.join()
        print "joining-R = DONE!"

    def addTank(self):
        self.t = Tank(self, 70, 100)
        self.t.draw()

    def update(self):
        ''' 
        Timer callback.
        Function to update the world (re-draw it)
        Return value defines the restart of the timer.
        '''
        self.__mark_update()
        return self.game.running

    def recalc(self):
        '''
        Timer callback.
        Function to re-calculate the world (re-position all the objects)
        Return value defines the restart of the timer.
        '''
        self.__mark_recalc()
        return self.game.running

    def __on_close(self):
        # print "STOP Updating"
        # self.timerUpdate.stop()
        # print "STOP Recalculating"
        # self.timerRecalc.stop()
        pass

    def __mark_update(self):
        print "UPDATING the world !"
        # z = self.canvas.create_oval(15, 5, 25, 15, fill="red")
        sleep(0.1) # 100 ms
        # self.canvas.delete(z)


    def __mark_recalc(self):
        print "RE-CALCULATING the world !"
        z = self.canvas.create_oval(45, 5, 55, 15, fill="yellow")
        sleep(0.1) # 100 ms
        self.canvas.delete(z)

