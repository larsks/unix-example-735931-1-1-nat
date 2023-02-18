#!/bin/sh
iptables -t raw -A PREROUTING -s 192.168.2.0/24 -i middleman-eth0 -j CT --zone-orig 100
iptables -t raw -A PREROUTING -s 192.168.2.0/24 -i middleman-eth1 -j CT --zone-orig 200
