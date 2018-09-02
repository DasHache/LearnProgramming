# Task 002.

# Part I. 1 point per correctly answered question.
# 
# 1. Let's keep remembering stuff... We are making a video game. What do we need? 
#
#    Note! It will help you to remember all these stuff better if
#          after each line of code described here, you STOP reading,
#          put this line into a file, save the file, run it and observe yourself.
#          DO NOT TRUST ANYONE! ALWAYS CHECK.
#
#          "EVERYBODY LIES" "EVERYBODY DIES"
#                          -- Gregory House, a great python programmer.
# 
#    Q: To draw stuff... How can we do it in python?
#    A: We need a library (written by some nice person for us) that 
#       would let us draw things on the screen and move them around. 
#
#    Q: Which graphic library/module we want to use? 
#    A: The one we already know a little - Tkinter
#
#    Q: How to import Tkinter and give it a shorter name?
#    A: import Tkinter as Tk
# 
#    Q: What do we need to do to start using it?
#    A: Initialize it by doing: a = Tk.Tk()
#
#    Q: What has just happened? What is Tk.Tk()? 
#    A: First "Tk" is how we access the module we imported.
#       Second "Tk" is the class located in that module
#       "()" after the second "Tk" is a "calling operator" = a way to call it.
#
#    Q: What happens when you "call" a class?
#    A: It invokes a special function of this class, called "__init__"
#       This function is also written for us by that nice guy who wrote the module
#       After that, we can start using Tkinter.
#
#    Q: What happens when you call a function? What's a function?
#    A: It is something that takes arguments and returns a result as an operation on these args.
#
#    Q: What will be the type of the returned result? "Tk.Tk()"
#    A: It will return an object of type Tk.
#
#    Q: What is "a" in "a = Tk.Tk()" ?
#    A: It is a variable which we can now use to access the created Tk object.
#
#    Q: What will be assigned to the variable "a"? "a = Tk.Tk()"
#    A: Object of type Tk.
#
#    Q: What do we need?
#    A: Create a canvas on which we are going to draw all the stuff.
#   
#    Q: How?
#    A: Tk.Canvas(initialized_tkinter_object, width=300, height=200)
#
#    Q: Where do we get the "initialized_tkinter_object"?
#    A: It's our "a" from above. We could have done it this way:
#       initialized_tkinter_object = Tk.Tk()
#
#    Q: How can we now use our canvas?
#    A: We cannot. We created it, but we forgot to assign it to a variable
#       our_canvas = Tk.Canvas(initialized_tkinter_object, width=300, height=200)
#
#    Q: How can we use it now?
#    A: canvas.create_rectangle(0, 20, 200, 100,  fill="light blue")
#
#    Q: What will we see if we put all these into a file and run it?
#    A: Nothing. We forgot to "pack" our canvas: canvas.pack()
#
#    Q: Now?
#    A: Still nothing. Actually, it did happen but so quickly that we didn't see it.
#
#    Q: Why the program exited?
#    A: We forget the "mainloop" - a function that never returns - a endless loop.
#
#    Q: Why is it a "loop"?
#    A: Because it repeatedly reads our actions (none for now) and changes the drawing accordingly.

import Tkinter as Tk
an_object_of_type_tkinter = Tk.Tk()
canvas = Tk.Canvas(an_object_of_type_tkinter, width=300, height=200)
canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
canvas.pack()
an_object_of_type_tkinter.mainloop()

# Now, apply all your knowledge in to the project.

# Open the file "xxx.py" and modify the function "yyy" in a such a way that
# "python game.py" would produce the same result as this file.
# (Of course "xxx" and "yyy" is NOT the real names ;)
# Yes, actually, you can run this file: python task_002.py




