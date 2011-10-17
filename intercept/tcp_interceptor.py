from scapy.all import sendp,Ether,TCP,IP
from tcp_state import *

class TcpInterceptor(object):
    def __init__(self, gateway_ip, gateway_mac, int_sock, bridge):
        self.gateway_ip = gateway_ip
        self.gateway_mac = gateway_mac
        self.int_sock = int_sock
        self.sockets = {}
        self.bridge = bridge

    def process_pkt(self, pkt):
        ip = pkt[IP]
        tcp = pkt[TCP]
        sock = (ip.src, tcp.sport, ip.dst, tcp.dport)
        print sock
        if sock in self.sockets:
            pass
        elif self.swap_socket(sock) in self.sockets:
            pass
        else:
            pass

    def swap_socket(self, s):
        return (s[2], s[3], s[0], s[1])

