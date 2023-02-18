#!/bin/sh
ip link add vrf-inner type vrf table 100
ip link add vrf-outer type vrf table 200
ip link set vrf-inner up
ip link set vrf-outer up
ip link set dev middleman-eth0 master vrf-inner
ip link set dev middleman-eth1 master vrf-outer
