from world import World
from handle import Handle
class Game:
    def __init__(self):
        print "I am a constructor of the class Game"
        w = World()
        h = Handle(w)
        w.run()
            
game = Game()        
 
