# Task 007 - Learn to handle keyboard and mouse

# 1. Change Timer value
#    Make Timer's period longer than 1 sec (now, you have 0.1 second, it's too fast)

# 2. Remove all console output
#    Comment out (add '#" sign at the beginning of the line) all text output. 
#    For now it prints "Hellow world" and "color = ..." to the terminal.

# 3. Add the handlers for keyboard and mouse
#    
#    3.1 Create a new file 'handle.py'
#
#    3.2 Add the following code into 'handle.py' (un-comment the lines)
#
##################### start of handle.py ########################
#
# class Handle:
#
#     def __init__(self, world):
#         self.canvas = world.canvas
#         self.canvas.bind("<Button-1>", self.handle_mouse)
#         self.canvas.bind("<Key>", self.handle_key)
#         self.canvas.focus_set()
#
#     def handle_key(self, event):
#         print "You pressed a key!"
#         if event.char == u'1':
#             print " ... key is '1'"
#         elif event.char == u'a':
#             print " ... key is 'a'"
#         else:
#             print " ... key is unknown"
#
#     def handle_mouse(self, event):
#         print "You clicked a mouse button."
#
##################### end of handle.py ########################
#
#    3.3 Look at the code of 'handle.py' and try to understand what it's doing
#        1. It's a class, called Handle
#        2. This class has 3 member-functions
#        3. Inside __init__ function it references the 2 other functions. Can you find it?
#        4. What __init__ function takes as an argument?
#        5. What is the type/class of the argument 'world' that it takes?
#        6. Which member-function object 'world' has?
#           ANSWER: It's type is unknown here, but it has a member 'canvas'. You can guess it's type is 'World'.
#        7. What is the type/class of the object 'world.canvas' ?
#           ANSWER: It's type is also unknown here. You can guess it's type is 'Tkinter.Canvas'
#        8. Which new method it calls?
#           ANSWER: Tkinter.Canvas.bind - It is a function that takes 2 arguments, right? 
#        9. What are the types of those arguments?
#           ANSWER: First is 'string', second is 'a function'
#       10. What are the values of those arguments? 
#           ANSWER: First gets value "<Key>" (it's a string), second 'self.handle_key' (it's a function).
#       11. Ignore the next line for now "self.canvas.focus_set()"
#
#    3.4 What is the idea here? 
#        1. It will call 'handle_mouse' function when you click a mouse.
#        2. It will call 'handle_key'   function when you press a key.
#
#    3.5 Study these 2 functions in the same way as you studied Handle.__init__() in paragraph "3.3".
# 
#
# 4. Add the following line in to 'game.py':
# 
#    from handle import *
#
#    And the following line also:
#
#    h = Handle(w)
#
#    Think carefully where exactly you need to put these lines in 'game.py'
#
# 5. The end.
# 
#    If you did right, you should see the following (if you click on canvas and press '1', 'a', 'b'):

####################################################################################################
#
# [kowaraj@ams-usba2eth001: ~/src/DasHache/LearnProgramming ] python game.py
# I am a constructor of the class Game
# I am a constructor of the class World
# You clicked a mouse button.
# You clicked a mouse button.
# You pressed a key!
#  ... key is '1'
# You pressed a key!
#  ... key is 'a'
# You pressed a key!
#  ... key is unknown
#
####################################################################################################








# ----->>>         You can ignore the rest, we will do it together later.      <<<------------

# 6. For the Git 
# 
# When you commit, be careful! You have added a new file: 'handle.py'
# 
# If you type 'git status' you will see the following:

####################################################################################################
# [kowaraj@ams-usba2eth001: ~/src/DasHache/LearnProgramming ] git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#   modified:   game.py
#   modified:   task/task_007.py
#   modified:   world.py
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#   handle.py
####################################################################################################

# Notice: 'Untracked files' and 'handle.py'

# Then, you need to add 'handle.py' to your repository:

####################################################################################################
# [kowaraj@ams-usba2eth001: ~/src/DasHache/LearnProgramming ] git add ./handle.py
# [kowaraj@ams-usba2eth001: ~/src/DasHache/LearnProgramming ] git status
# On branch master
# Your branch is up-to-date with 'origin/master'.
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#   new file:   handle.py
####################################################################################################


# Now you can commit:

####################################################################################################
# [kowaraj@ams-usba2eth001: ~/src/DasHache/LearnProgramming ] git commit -m "Add file 'handle.py'"
# [master 30e39cc] Add file 'handle.py'
#  1 file changed, 19 insertions(+)
#  create mode 100644 handle.py
####################################################################################################


# ... and push.
