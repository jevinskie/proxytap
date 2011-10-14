#!/usr/bin/env python

from scapy.all import sniff,ARP
from arp_interceptor import *
import sys

tap_if = sys.argv[1]
gateway_ip = sys.argv[2]
gateway_mac = sys.argv[3]

arp_int = ArpInterceptor(gateway_ip, gateway_mac, tap_if)



def intercept_packet(pkt):
    print "got packet"
    pkt.show()
    if ARP in pkt and pkt[ARP].op == 1:
        # arp lookup
        arp_int.process_req(pkt)
    return None

sniff(prn=intercept_packet, store=0, iface=tap_if)

