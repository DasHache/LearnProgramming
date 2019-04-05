
class Tank:

    def __init__(self, the_world_I_live_in, my_initial_position_x, my_initial_position_y):
        print "Hi, I am an instance of the Tank class"
        self.w = the_world_I_live_in
        self.x = my_initial_position_x
        self.y = my_initial_position_y
        self.s = 40  # This is my size
        self.bangle = 0 # This is the initial angle of my barrel
        self.blen = 50 # lenght of my barrel
        self.b = None # This will be my barrel
        
    def draw(self):

        # Drawing a tank
        d = self.s/2
        tank_x1 = self.x - d
        tank_y1 = self.y - d
        tank_x2 = self.x + d
        tank_y2 = self.y + d
        self.w.canvas.create_rectangle(tank_x1, tank_y1, tank_x2, tank_y2, fill="red")


    
