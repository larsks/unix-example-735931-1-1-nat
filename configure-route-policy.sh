#!/bin/sh
ip rule add prio 100 fwmark 100 lookup 200
ip rule add prio 200 fwmark 200 lookup 100
