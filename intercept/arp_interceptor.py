from scapy.all import sendp,Ether,ARP

class ArpInterceptor(object):
    def __init__(self, gateway_ip, gateway_mac, tap_if):
        self.gateway_ip = gateway_ip
        self.gateway_mac = gateway_mac
        self.tap_if = tap_if

    def process_req(self, pkt):
        a = pkt[ARP]
        if a.pdst == self.gateway_ip:
            res = Ether(src=self.gateway_mac, dst=a.hwsrc)/ARP(op="is-at",
                        psrc=self.gateway_ip, hwsrc=self.gateway_mac,
                        pdst=a.psrc, hwdst=a.hwsrc)
            sendp(res, iface=self.tap_if)

