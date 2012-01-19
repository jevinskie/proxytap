#!/usr/bin/env python

import sys
import SocketServer
import threading

class ThreadingUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer): 
     allow_reuse_address = True

class EchoHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        print "%s wrote:" % self.client_address[0]
        print data,
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    port = int(sys.argv[1])

    server = ThreadingUDPServer(("0.0.0.0", port), EchoHandler)

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    while True:
        try:
            # long timeout to allow for signals with minimal polling
            thread.join(2**31)
        except KeyboardInterrupt:
            break

