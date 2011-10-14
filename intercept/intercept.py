#!/usr/bin/env python

from scapy.all import *
from arp_interceptor import *
from tcp_interceptor import *
import pyev
import sys
import signal

tap_if = sys.argv[1]
gateway_ip = sys.argv[2]
gateway_mac = sys.argv[3]

arp_int = ArpInterceptor(gateway_ip, gateway_mac, tap_if)
#tcp_int = TcpInterceptor(gateway_ip, gateway_mac, tap_if)

L2socket = conf.L2listen
s = L2socket(iface=tap_if)

def intercept_packet(watcher, revents):
    global s
    print "got packet"
    pkt = s.recv(MTU)
    if pkt == None:
        return
    pkt.show()
    if ARP in pkt and pkt[ARP].op == 1:
        # arp lookup
        arp_int.process_req(pkt)
    if TCP in pkt:
        # tcp intercept
        #tcp_int.process_pkt(pkt)
        pass
    return

def sig_cb(watcher, revents):
    print "got SIGINT"
    loop = watcher.loop
    # optional - stop all watchers
    if loop.data:
        print "stopping watchers: %r" % loop.data
        while loop.data:
            loop.data.pop().stop()
    # unloop all nested loop
    print "stopping the loop: %r" % loop
    loop.stop(pyev.EVBREAK_ALL)

# event loop stuff goes here

loop = pyev.default_loop()

io = loop.io(s, pyev.EV_READ, intercept_packet)
io.start()
sig = loop.signal(signal.SIGINT, sig_cb)
sig.start()
loop.data = [io, sig]
loop.start()

