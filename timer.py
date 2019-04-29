from threading import Timer

class InfiniteLoopTimer:

    def __init__(self, w, obj, obj_method_name, dt=1):
        self.stopped = False
        self.o = obj
        self.omn = obj_method_name
        self.dt = dt

    def start(self):
        self.t = Timer(self.dt, self.callback)
        self.t.start()

    def callback(self):
        ''' 
        This function gets called whtn the timer elapses.
        1. It calls the callback function: self.omn
        2. If callback return value (keep_running) is True, 
           it means the game is ON.
           Then we re-Start the timer by: self.start
        3. If the callback return value is False, 
           we do NOT re-start the timer. 
           Then the world will not be neither updated nor re-calculated
        '''
        
        keep_running = getattr(self.o, self.omn)()
        if keep_running:
            self.start()


