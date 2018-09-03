# As an advise: Before you start reading the task, start a stopwatch.
#               And stop it once you're done. Write down the time it
#               took: 
#               - to undertand the task
#               - to complete the task
#               And add a comment why it took longer (or shorter)
#               then it might have taken. 
#               - Were you distracted by a cat?
#                 (Don't hurt the cat, it's not his fault.)
#               - The teacher doesn't explain good enough?
#               - Any other reason? 
# 
# Whenever you do something... 
# It is VERY important to KNOW how much time/effort you will spend
# and how much resources/pleasure you will obtain for that.


# Task 003. 5 points.

# Part I.
# Let's stop for a second and think what we have already done.
#
# Here is the list:
# - Game (game.py)
#     Class Game is the main class of the game we are writing.
#  
#     It is the starting poing of everything. Have you read the Bible?
#     You should. It's a nice science fiction story!
#     In short, it goes like this. There was a bored guy, called God.
#     He had nothing to do and one day he decided to entertain himself.
#     So, he started writing a game. On the first day he created a world.
#     The world is a place where everything else would be placed later 
#     (like: ground, water, sky, people and all other stuff)...
# 
#     So, you, Dasha the God, created the file "world.py" where you put 
#     the class World. Then, you started creating the ground, the sky and
#     the water (which would be your "light blue" rectangle - canvas).
#     You are not a very experienced god yet, so you created a very simple
#     World. Not bad for the first version though.
#     
#     However, you put it to the wrong place. You put it to the class Game. 
#     Yeah, yeah.. I know, it's my mistake. However, you could have already
#     started using your own brain and think what you were doing. 
#     Anyways, let's fix this. 
#     Just remove it from the Game and put it to the World's constructor.
# 
#     Done? Good. 
# 
#     Now, what you have is:
# 
#     - game.py (a file)
#       - Game (a class)
#         - __init__ (a function)
#           It creates an object of class World. Nothing else. 
#       - game (a variable)
#         It is assigned to an object of the class Game by "game = Game()"
#
#     - world.py (a file)
#       - World (a class)
#         - __init__ (a function)
#           It creates your simple version of the world, a canvas.
# 
#     Everything is clear? 
# 
#     Question?
#     If you are not sure you understand something, you ask. 
#     Also, you can write your questions/comments in this file, below. 
# 
#     For example:
#     I would like to know how to turn water into wine.
#     When will I know kung-fu? 
#     Why am I doing all this?

# Part II.
# There is one thing you should remember. 
# Programming is not about typing your code into the files. 
# Programming is engineering. Engineering is mostly about the design.
# Design as a process. As an algorithm you choose to achieve your goal.
# So, before you type, you think. 
# You think about:
# - What is your goal?
# - How can you get there? 
# - What do you need for that?
# - What do you know? 
# - What have your learned before that might help you?
# - What do you NOT know? 
# - What else will you have to learn?
# 
# For example, look at the constructor of the World class, the __init__ function.
# Question : What does it do? 
# Answer   : It creats the world and runs it.
# 
# Do you understand that those are 2 separate things? 
# It's like you build a domino sequence and then you run it:
# Check this out:
# https://www.youtube.com/watch?v=XWMd3tyAngk 
# https://www.youtube.com/watch?v=1QtdPfz_faM
# 
# You see? There are 2 different things. Build. Then run. 
# But you have it all together. In the same function. 
# That's ok for now. It's ok because you function is not 100 lines long.
# And you don't have 1000 of functions in your program. Yet. 
# So, it's easy to understand what the function is doing. 
# It will be harder later, trust me. Unless you split it
# into 2 separate functions - "build" and "run". 
# Build is generally called "construct" in programming and done by the 
# constructor. In python, constructors called "__init__".
# 
# This means the first part of your code is in the right place.
# And you keep it there. What is the "run" part of your code? 
# 
# 1.       # world = World()
# 2.       # a = Tk.Tk()
# 3.       # canvas = Tk.Canvas(a, width=300, height=200)
# 4.       # canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
# 5.       # canvas.pack()
# 6.       # a.mainloop()
# 
# Question : Which lines (from 1 to 6) belong to the "run" part? 
# Anwer    : Only line #6. 
# 
# Why? What is line #6 doing? Think. Recall. If lazy, look for the answer 
# in the task_002.py file. There is a question about that with the answer.
# 
# Finally, your task is to separate the "run" part of the constructor's code 
# into a separate member-function of the class World, named run.




