from scapy.all import sendp,Ether,ARP

class ArpInterceptor(object):
    def __init__(self, gateway_ip, gateway_mac, int_sock):
        self.gateway_ip = gateway_ip
        self.gateway_mac = gateway_mac
        self.int_sock = int_sock

    def process_pkt(self, pkt):
        a = pkt[ARP]
        # op is a arp lookup
        if a.op == 1 and a.pdst == self.gateway_ip:
            res = Ether(src=self.gateway_mac, dst=a.hwsrc)/ARP(op="is-at",
                        psrc=self.gateway_ip, hwsrc=self.gateway_mac,
                        pdst=a.psrc, hwdst=a.hwsrc)
            self.int_sock.send(res)

