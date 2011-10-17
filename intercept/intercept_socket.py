from scapy.all import conf


class InterceptSocket(conf.L2socket):
    def __init__(self, tap_if):
        conf.L2socket.__init__(self, iface=tap_if)

