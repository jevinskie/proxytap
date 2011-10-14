from scapy.all import sendp,Ether,TCP
from tcp_state import *

class TcpInterceptor(object):
    def __init__(self, gateway_ip, gateway_mac, tap_if, bridge):
        self.gateway_ip = gateway_ip
        self.gateway_mac = gateway_mac
        self.tap_if = tap_if
        self.sockets = {}
        self.bridge = bridge

    def process_pkt(self, pkt):
        ip = pkt[IP]
        tcp = pkt[TCP]
        socket = {'src_ip': ip.src, 'src_port': tcp.sport,
                  'dst_ip': ip.dst, 'dst_port': tcp.dport}
        if socket in self.sockets:
            pass
        elif self.swap_socket(socket) in self.sockets:
            pass
        else:
            pass

    def swap_socket(s):
        return {'src_ip': s['dst_ip'], 'src_port': s['dst_port'],
                'dst_ip': s['src_ip'], 'dst_port': s['src_port']}
            
