from scapy.all import Ether,TCP
import socket
from tcp_state import *

class PlainTcpBridge(object):
    def __init__(self):
        self.sockets = {}

    def set_tcp_interceptor(self, tcp_int):
        self.tcp_int = tcp_int

    def connect(self, sock):
        try:
            print "start con"
            brsock = socket.create_connection(sock[2:4])
            print "finished con"
            if self.tcp_int.finish_connect(sock):
                self.sockets[sock] = {'state': tcp_states.ESTABLISHED}
        except Exception, e:
            print e

