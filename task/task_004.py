# Task 004. Nothing to be done. Something to be understood. 

# So, what is the "scope"? 
#
# More precisely the "scope of a name binding" is....
# well, let's find out what we already know.
# We do not know what "scope" or "binding" mean. But we do know what is a name.
# Actually, a name of a variable. Like here:
a = 5

# Here, "a" is a variable. Its name is... well, "a". 
# What is its value? Correct, it's 5.
# What is "="? Correct, it's an operator (a function).
# This function binds a value "5" to a name "a". It creates a "binding".

# If you try the following:
print "x = " + x
x = 15

# ... you will get an error:
# >>  NameError: name 'x' is not defined

# When python executes the code "print 'x = ' + x" it EVALUATES the 
# things it knows. And here, it already knows that:
#   print   - is a function
#   "x = "  - is a string
#   +       - is another function
# 
# But it does NOT know what 'x' is! And it cannot EVALUATE it. 
# Remember? It executes line after line (in this case). 

# If you try this:
y = 15
print "y = " + y

# ... no errors! Python already knows how to EVALUATE 'y' when it needs to.
# So far it should be easy. Just pay attention to the terminology. 
# By now, you should understand 2 out of 3 words in "scope of a name binding"
# You have a name. You make python bind it to a value. Everybody is happy. 

# So, what is the scope?...

# I will try to explain this with an analogy. Imagine a video game.
# There is a super-monster in a dangeon. You have to kill it. 
# The dangeon is 3 levels deep. 
# First, you get to level 1. Then level 2. Then 3. 
# When you kill it you have to bring his heart back to a sorcerer in the town.
# To leave the dangeon, from level 3 you get to level 2, then to level 1. Then out. 
# Ok? No teleports, no escalators, no other way to change the path. 
#
# What else.. Ah, on each level there is a special type of lesser daemons. 
# Level 1: Deamons can only be killed by water.
#          When you enter level 1 you are given a scroll with water magic spells. 
# Level 2: These guys are only killed by fire (or water).
#          When you enter level 2 you are given a scroll with fire spells.
# Level 3: Let's say, here you will also need the air magic. 
#          Same story. You enter, you get some air magic. 
# 
# Now. You can only kill the super-monster with a super-weapon.
# To get the super-weapon you have to combine all 3 types of spells together.
# 
# Sound easy, right? 
#
# Let's add a twist. When you leave a level (on your way back home) you have to 
# put back the spell scroll on its place (where you found it). Otherwise, it will not 
# let you out.
# 
# And there is still no problem.
# The rules look reasonable. The game looks playable. It should be a piece of cake. 
# 
# Where was I?... Oh, right. The "scope". 
# 
# Imagine a mistake in the game. 
# 
# Mistake #1. When you enter the level 1 you see a water deamon.
#             Obviously, you cannot kill water daemon with a water spell. Game over. 
#             (No, you can NOT run away from it. It's a very fast water daemon.
#             Stop thinking about a way to win and pay attention to the idea! ;) 
#             The idea is that you can NOT use air or fire magic here. You have not
#             learned them yet. You will. Later. On the levels 2 and 3. 
#             
# Mistake #2. You have passed all 3 levels. You have killed the super-guy. You get to 
#             the exit from level 3. You leave you air magic spell here. You get to the 
#             level 2 and... Here it is! A water-and-fire-immune deamon! You need an air spell.
#             Heeelp! Game over. (Yes, also a very fast air daemon. No way to escape or kill it.)
#             Yes, you DID have the spell, but you have un-learned it when exited level 3. 
#             The idea is that that air spell was DEFINED in the level 3. 
#             Level is would be called the "scope" of the air spell.
#             It means that the air spell is only available (VALID) on the level 3.
#
#             A very important point here! You are still on the level 2. Just left the level 3.
#             Let's say there is no water-and-fire-immune deamon this time. Only a fire-immune one.
#             Would it be a problem? 
#             You could have killed it with the air spell, but you have left it on the level 3.
#             You only learned the fire magic on the level 2. It wouldn't work. 
#             A water spell would come in handy! Do you have one? Yes! You learned it on the level 1.
#             And you will have to un-learn it, but only when you leave the level 2.
#             But here, on the level 2, this spell is still in its "scope". 
#             In other words, YOU HAVE NOT YET LEFT ITS SCOPE. You can use it. 
#             You are safe!

# Same with the variable, functions and classes.
# Run:
#   python ./snippets/task_004/dangeon_v2.py
#
# Look into the files
# - ./snippets/task_004/dangeon_v2.py
# - ./snippets/task_004/dangeon_v2_funcs.py

# The most important thing you need to understand is what python consider a "level".
# When you call a function in your code and 
# python ENTERS this function -> it goes 1 level DOWN. 
# python EXITS  the  function -> it goes 1 level back. One level UP.

# When python ENTERS a function (goes 1 level DOWN), 
# and if you call another function from the 1st function (python goes 1 MORE level DOWN).

# Consider this code:

def f2():
    print "in f2"

def f1():
    print "in f1"
    f2()

# And you call "f1" which, in turn, calls "f2" like this:
f1()

# Then, inside the function "f2" it would be on the level 2. Inside the f1, on the level 1."

# Is it not clear?
# It's ok. Do not worry.
# We will get back to it many times later. It's not that simple.

# But now, let's get back to the problem in task_003.py.
# Why this gives you an error? 

import Tkinter as Tk
class World:
    def __init__(self):
        a = Tk.Tk()
        canvas.create_rectangle(20, 20, 260, 160,  fill="light blue")
        canvas.pack()

    def run(self):
        a.mainloop() # ERROR is HERE !!! Variable 'a' is NOT BOUND !!!

# Let's think. You ENTER the level (scope) called "run". Which magic do you have here?
# 1. You have variable "self" which is bound to something. 
# 2. Also, you have everything imported from Tkinter (by the first line).
#    Why? Because this magic you brought from the previous "level" (scope). 
# And... nothing else.
# Variable 'a' is not found! 
# 
# Ok. It's easy to fix. 
# Normal way to do this (when we are in a class) is the following.

class A:
    def __init__(self):
        self.a = 5                 # <------ self.a

    def run(self):
        print "a = ", self.a       # <------ self.a 

# What have we done? Why now 'a' is an error? How does python know what it is? 
# What is it BOUND to? 
# The correct answer would be that "There is NO variable a".
# But, "a" is a MEMBER of the class "A". 
# And "self" is just a "pointer" to the object of class A.
# Think of "self" as a way TO GET ACCESS to 'a'.
# As long as you are inside the class "A" you can access "a" with "self.a".

# Now, you should be able to solve the problem. Fix the file "world.py".






