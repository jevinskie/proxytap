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
        hwsrc = self.get_hwsrc(pkt)
        tcp = pkt[TCP]
        sock = self.get_socket(pkt)
        print sock
        if sock in self.sockets:
            pass
        elif self.swap_socket(sock) in self.sockets:
            print "how did this happen, saw incoming traffic"
        else:
            print "connecting"
            self.sockets[sock] = {'hwsrc': hwsrc, 'state': tcp_states.SYN_SENT}
            self.bridge.connect(sock)

    def swap_socket(self, sock):
        return (sock[2], sock[3], sock[0], sock[1])

    def get_hwsrc(self, pkt):
        eth = pkt[Ether]
        return eth.src

    def get_socket(self, pkt):
        ip = pkt[IP]
        tcp = pkt[TCP]
        return (ip.src, tcp.sport, ip.dst, tcp.dport)

    def send(self, sock, data):
        pass

    def finish_connect(self, sock):
        sock_state = self.sockets[sock]
        self.int_sock.send(Ether(src=self.gateway_mac, dst=sock_state['hwsrc'])/IP(
            dst=sock[0], src=sock[2])/TCP(sport=sock[1], dport=sock[3], flags='SA'))
        return True

