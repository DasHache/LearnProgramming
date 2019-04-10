class Charge:

    def __init__(self, tank):
        print "Hi, I am an instance of the Charge class"
        self.t = tank # This if the tank that I belong to
        self.s = 10. # This is my size
        coords = tank.end_of_barrel 

        # What is the type of 'self.coords' ? 
        # It is an array. It contains 2 numbers.
        # To get the first number, use coords[0]
        # To get the second number, use coords[1]
        self.x = coords[0] # This is the X coordinate of the charge
        self.y = coords[1] # This is the Y coordinate of the charge

        self.id_on_canvas = None # This is my ID on the canvas

        self.__draw()

    def __draw(self):
        z = self.s/2. # a half of my size
        x1 = self.x -z
        x2 = self.x +z
        y1 = self.y -z
        y2 = self.y +z
        self.id_on_canvas = self.t.w.canvas.create_oval(x1, y1, x2, y2, fill="yellow")

        


        
