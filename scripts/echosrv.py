#!/usr/bin/env python

import sys
import SocketServer
import threading

class ThreadingTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer): 
     allow_reuse_address = True

class EchoHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if len(data) != 0:
                print "%s wrote:" % self.client_address[0]
                print data,
                self.request.send(data.upper())
            else:
                break

if __name__ == "__main__":
    port = int(sys.argv[1])

    server = ThreadingTCPServer(("0.0.0.0", port), EchoHandler)

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    while True:
        try:
            # long timeout to allow for signals with minimal polling
            thread.join(2**31)
        except KeyboardInterrupt:
            break

