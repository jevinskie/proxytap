#!/usr/bin/env python

from scapy.all import ARP,TCP
from arp_interceptor import *
from tcp_interceptor import *
from intercept_loop import *
import sys

tap_if = sys.argv[1]
gateway_ip = sys.argv[2]
gateway_mac = sys.argv[3]

arp_int = ArpInterceptor(gateway_ip, gateway_mac, tap_if)
#tcp_int = TcpInterceptor(gateway_ip, gateway_mac, tap_if)

def intercept_packet(pkt):
    print "got packet"
    pkt.show()
    if ARP in pkt:
        # arp intercept
        arp_int.process_req(pkt)
    if TCP in pkt:
        # tcp intercept
        #tcp_int.process_pkt(pkt)
        pass
    return

loop = InterceptLoop(intercept_packet, tap_if)
loop.start()

