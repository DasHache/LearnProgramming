import Tkinter as Tk

print "which color do you want for the background?"
color = raw_input("blue, red, brown, white, black?")
canvas = Tk.Canvas(width=300, height=300, bg=color)
canvas.pack()

ground = canvas.create_rectangle(300, 300, 0, 250, fill='brown')

figure = raw_input("what figure do you want to create?")
color2 = raw_input("wich color?")

if figure == 'rectangle':
   canvas.create_rectangle(20, 90, 40, 30, fill=color2)
elif figure =='square':
     canvas.create_rectangle(20, 90, 40, 30, fill=color2)
elif figure =='circle':
     canvas.create_rectangle(20, 90, 40, 30, fill=color2)
elif figure =='oval':
     canvas.create_rectangle(20, 90, 40, 30, fill=color2)


canvas.mainloop()