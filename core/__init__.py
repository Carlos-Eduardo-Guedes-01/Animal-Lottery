from threading import Thread
from time import sleep
class IntervalRunner(Thread):
    def __init__(self, interval, function, *args, **kwargs):
        super(self, IntervalRunner).__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.executing = False
    def run(self):
        self.executing = True
        while self.executing:
             self.function(*self.args, **self.kwargs)
             time.sleep(self.interval)

    def stop(self):
       self.executing = False