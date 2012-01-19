#!/usr/bin/env python

import sys
import SocketServer
import threading

class ThreadingUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer): 
     allow_reuse_address = True

class EchoHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        sock = self.request[1]
        cli_ip, cli_port = self.client_address
        srv_ip, srv_port = sock.getsockname()
        print "%s:%s -> %s:%s  got:" % (cli_ip, cli_port, srv_ip, srv_port),
        print data,
        sock.sendto(data.upper(), self.client_address)
        print "%s:%s -> %s:%s sent:" % (srv_ip, srv_port, cli_ip, cli_port),
        print data.upper(),

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

