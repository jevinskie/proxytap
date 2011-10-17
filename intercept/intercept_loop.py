import pyev
import signal
import sys


class InterceptLoop(object):
    def __init__(self, int_cb, int_sock):
        self.sock = int_sock
        
        loop = pyev.default_loop()
        
        io = loop.io(int_sock, pyev.EV_READ, self.io_cb)
        io.start()
        
        sig = loop.signal(signal.SIGINT, self.sig_cb)
        sig.start()
        
        loop.data = [io, sig]

        self.loop = loop

        self.int_cb = int_cb

    def start(self):
        self.loop.start()

    def sig_cb(self, watcher, revents):
        loop = watcher.loop
        # optional - stop all watchers
        if loop.data:
            print "stopping watchers: %r" % loop.data
            while loop.data:
                loop.data.pop().stop()
        # unloop all nested loop
        print "stopping the loop: %r" % loop
        loop.stop(pyev.EVBREAK_ALL)

    def io_cb(self, watcher, revents):
        pkt = self.sock.recv()
        if pkt == None:
            return
        else:
            self.int_cb(pkt)

