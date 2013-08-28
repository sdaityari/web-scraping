import threading
import sys

class TimeoutError(Exception): pass

def timelimit(timeout):
    def internal(function):
        def internal2(*args, **kw):
            class Calculator(threading.Thread):
                def __init__(self):
                    threading.Thread.__init__(self)
                    self.result = None
                    self.error = None
                
                def run(self):
                    try:
                        self.result = function(*args, **kw)
                    except:
                        self.error = sys.exc_info()[0]
            
            c = Calculator()
            c.start()
            c.join(timeout)
            if c.isAlive():
                try:
                    c._Thread__stop()
                except Exception as e:
                    print 'Thread can not be stopped'
                raise TimeoutError
            if c.error:
                raise c.error
            return c.result
        return internal2
    return internal
