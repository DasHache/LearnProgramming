import Tkinter as Tk
from threading import Timer


class World:
    def __init__(self):
        print "I am a constructor of the class World"
        self.a = Tk.Tk()
        canvas = Tk.Canvas(self.a, width=300, height=200)
        self.canvas = canvas
        self.x = 150
        self.x1 = 130
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.create_rectangle(20, 160, 80, 100,  fill="black")
        canvas.create_rectangle(50, 120, 100, 80,  fill="red")
        canvas.create_rectangle(80, 100, 150, 100,  fill="brown")
        self.id_charge = canvas.create_oval(self.x, 110, self.x1, 90, fill="yellow")
        canvas.pack()
        
        
    def run(self):

        t = Timer(1.0, self.hi)
        t.start()

        self.a.mainloop()


    def hi(self):
        print "Hello world"
       	current_color=self.canvas.itemcget(self.id_charge, 'fill')
        print 'color = ', current_color 
        
        if current_color == 'yellow':
            self.canvas.itemconfigure(self.id_charge, fill='red')
        if current_color == 'red':
            self.canvas.itemconfigure(self.id_charge, fill='blue')
        if current_color == 'blue':
            self.canvas.itemconfigure(self.id_charge, fill='red')
            
        self.canvas.coords(self.id_charge, self.x+10, 110, self.x1+10, 90)
        self.x = self.x+10
        self.x1 = self.x1+10
        t = Timer(1.0, self.hi)
        t.start()
        

    
    
        
