from charge import Charge

class Tank:

    def __init__(self, the_world_I_live_in, my_initial_position_x, my_initial_position_y):
        print "Hi, I am an instance of the Tank class"
        self.w = the_world_I_live_in
        self.x = my_initial_position_x
        self.y = my_initial_position_y
        self.s = 40  # This is my size
        self.blength = 50 # lenght of my barrel
        self.b = None # This will be my barrel
        self.charge_velocity = 20 # [m/s] initial velocity of a charge (power) ! will be a tuple
        self.c = None # no charge yet

    def draw(self):
        # Drawing a tank
        d = self.s/2
        x1 = self.x - d
        y1 = self.y - d
        x2 = self.x + d
        y2 = self.y + d
        self.w.canvas.create_rectangle(x1, y1, x2, y2, fill="red")

        # Drawing a barrel
        self.bx1 = x1 + (x2 - x1)/2
        self.by1 = y1 + (y2 - y1)/2
        self.bx2 = self.bx1 + self.blength
        self.by2 = self.by1 + 0
        self.__drawBarrel()

        # We will need this to draw the charge
        self.end_of_barrel = [self.bx2, self.by2] # The type of this is 'array'

        # Drawing a charge
        self.c = Charge(self)

    def __drawBarrel(self):
        self.b = self.w.canvas.create_line(self.bx1, self.by1, self.bx2, self.by2, fill="grey", width=3)


    def recalc(self):
        if self.c:
            self.c.recalc()

    def update(self):
        if self.c:
            self.c.update()


    
