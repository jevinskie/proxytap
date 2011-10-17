#!/usr/bin/env python

from scapy.all import ARP,TCP
from arp_interceptor import *
from tcp_interceptor import *
from plain_tcp_bridge import *
from intercept_loop import *
from intercept_socket import *
import sys

tap_if = sys.argv[1]
gateway_ip = sys.argv[2]
gateway_mac = sys.argv[3]

int_sock = InterceptSocket(tap_if)

arp_int = ArpInterceptor(gateway_ip, gateway_mac, int_sock)
tcp_bridge = PlainTcpBridge()
tcp_int = TcpInterceptor(gateway_ip, gateway_mac, int_sock, tcp_bridge)

def intercept_packet(pkt):
    print "got packet"
    pkt.show()
    if ARP in pkt:
        # arp intercept
        arp_int.process_pkt(pkt)
    if TCP in pkt:
        # tcp intercept
        tcp_int.process_pkt(pkt)
    return

int_loop = InterceptLoop(intercept_packet, int_sock)
int_loop.start()


