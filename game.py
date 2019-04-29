from world import World
from handle import Handle

import signal
import sys

class Game:
    def __init__(self):
        print "I am a constructor of the class Game"
        self.running = True
        self.w = World(self)

        # Add a signal handler:
        # When you press Control + C, python will call self.signal_handler
        signal.signal(signal.SIGINT, self.signal_handler)
        
        h = Handle(self.w)
        self.w.run()

        print "World exited."
        sys.exit(0)

    def signal_handler(self, sig, frame):
        '''
        This functions gets called when a user presses Ctrl+C
        To quit the game, We need to stop the mainloop
        '''
        print('You pressed Ctrl+C!')
        self.running = False
        self.w.stop_mainloop()
        print('Your game will soon be OVER.')

            
game = Game()        
 
