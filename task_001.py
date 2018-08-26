# Task 001. Single task. 5 point.
# 
# 1. Create a file "world.py".
# 2. Put the following code in this file:
#    - Create an "empty" class with name "World".
#      Empty class is a class that has minimum stuff in it, 
#      but is still considered to be a class by Python.

class World:
    def __init__(self):
        pass

# 3. Make python execute this file and see what happens.
#    In a terminal: python a.py

# 4. Nothing happened, right? Why? What really happened?
#    Yes, you need to think sometimes.

# 5. Have you been thinking? Good.
#    So you realized that
#    - python started, 
#    - then it read your file,
#    - it found a class
#    - it understood that you will use this class (a.k.a. data type)
#    - it didn't find anything else
#    - it exited

# 6. Let's create another class in another file
#    1. Import class "World" from file "world"
#    2. Create an "empty" class with name "Game"
#    3. Create and object of type "Game" with name "game"

from world import World

class Game:
    def __init__(self):
        pass

game = Game()

# 7. Run it with: python game.py
#    Still nothing happens, right? Why?

# 8. Correct answer:
#    - We didn't ask python to do anything it can show.
#    It did a lot, but didn't show anything.
#   
#    Now, let's make it show what it does
#    Change the definition of the CONSTRUCTOR function of your "World" class.
#    Yes, __init__ is the constructor.
#    Instead of "pass" (which means do nothing) put 
#    print "I am a constructor of the class World"
# 
#    Do the same for the Game class:
#    Instead of "pass" put 
#    print "I am a constructor of the class Game"


# 9. Run it with: python game.py
#    You should see in the terminal something like this:
#
#    [: ~/src/LearnProgramming ] python game.py
#    I am a constructor of the class Game
#    [: ~/src/LearnProgramming ] 
# 
#    Why don't you see the constructor of the World class?
#    Correct answer: We didn't ask for it. 
#    This is you task! 
#    Remember, you still have to call "python game.py" 
#    What do you need to add and to which file, to see this:
# 
#    [: ~/src/LearnProgramming ] python game.py
#    I am a constructor of the class Game
#    I am a constructor of the class World
#    [: ~/src/LearnProgramming ]













