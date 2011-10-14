from enum import enum

tcp_states = enum('CLOSED', 'SYN_SENT', 'SYN_RECV', 'LISTEN',
    'ESTABLISHED', 'CLOSE_WAIT', 'LAST_ACK', 'FIN_WAIT1', 'FIN_WAIT2',
    'CLOSING', 'TIME_WAIT')

