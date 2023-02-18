#!/bin/sh
iptables -t nat -A PREROUTING -d 192.168.3.0/24 -j NETMAP --to 192.168.2.0/24
iptables -t nat -A POSTROUTING -s 192.168.2.0/24 -j NETMAP --to 192.168.3.0/24
iptables -t mangle -A PREROUTING -i middleman-eth0 -d 192.168.3.0/24 -j MARK --set-mark 100
iptables -t mangle -A PREROUTING -i middleman-eth1 -d 192.168.3.0/24 -j MARK --set-mark 200
