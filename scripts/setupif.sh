#!/bin/sh

ip tuntap add dev tap0 mode tap
brctl addbr br0
brctl addif br0 tap0
ip link set dev tap0 up
ip link set dev br0 up

