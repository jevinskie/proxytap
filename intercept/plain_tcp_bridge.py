from scapy.all import sendp,Ether,TCP

class PlainTcpBridge(object):
    def __init__(self):
        pass

    def process_pkt(self, pkt):
        t = pkt[TCP]

