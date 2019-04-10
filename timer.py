from threading import Timer

class InfiniteLoopTimer:

    def __init__(self, w, obj, obj_method_name, dt=1):
        self.stopped = False
        self.o = obj
        self.omn = obj_method_name
        self.dt = dt

    def start(self):
        if self.stopped:
            return

        self.t = Timer(self.dt, self.callback)
        self.t.start()

    def callback(self):
        getattr(self.o, self.omn)()
        self.start()

    def stop(self):
        self.t.cancel()
        self.stopped = True
