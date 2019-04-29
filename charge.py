import time
from math import sin, cos, pi

class Charge:

    def __init__(self, tank):
        print "Hi, I am an instance of the Charge class"
        self.c = tank.w.canvas
        self.t0 = time.time()
        self.s = 10.
        self.d = (0.,0.) # [m, m] --- coord. delta tuple

        # What is the type of 'self.coords' ? 
        coords = tank.end_of_barrel # [m, m] --- coord tuple
        # It is an array. It contains 2 numbers.
        # To get the first number, use coords[0]
        # To get the second number, use coords[1]
        self.x = coords[0] # This is the X coordinate of the charge
        self.y = coords[1] # This is the Y coordinate of the charge
        self.dx = 0
        self.dy = 0

        z = self.s/2. # a half of my size
        x1 = self.x -z
        x2 = self.x +z
        y1 = self.y -z
        y2 = self.y +z

        self.id_on_canvas = self.c.create_oval(x1, y1, x2, y2, fill="yellow")

        self.v = [tank.charge_velocity, 0] # [m/s, m/s] --- velocity tuple

    def update(self):
        z = self.s / 2.
        x = self.x + self.dx
        y = self.y + self.dy
        x1 = x -z
        x2 = x +z
        y1 = y -z
        y2 = y +z
        self.c.coords(self.id_on_canvas, x1, y1, x2, y2) # move the charge

        # This is just to keep track of the charge trajectory
        __trace = self.c.create_oval(x-1,y-1,x+1,y+1, fill="grey")

    def recalc(self):
        dt = self.gettime()
        self.dx = self.v[0] * dt
        self.dy = self.v[1] * dt + 9.8 * dt * dt 

    def gettime(self):
        dt = time.time() - self.t0
        print 'dt = ', dt
        return dt/5.
        
