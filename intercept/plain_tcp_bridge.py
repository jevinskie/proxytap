from scapy.all import sendp,Ether,TCP

class TcpInterceptor(object):
    def __init__(self, gateway_ip, gateway_mac, tap_if):
        self.gateway_ip = gateway_ip
        self.gateway_mac = gateway_mac
        self.tap_if = tap_if
        self.sockets = {}

    def process_pkt(self, pkt):
        t = pkt[TCP]

