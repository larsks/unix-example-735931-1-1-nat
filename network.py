from topology import Custom

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.topo import Topo
from mininet.log import info, error, setLogLevel

if __name__ == '__main__':
    setLogLevel("info")

    topo = Custom()
    net = Mininet(topo=topo, switch=OVSBridge)
    net.start()

    middleman = net.nameToNode['middleman']

    for script in ["configure-vrf.sh", "configure-route-policy.sh", "configure-nat.sh", "configure-conntrack.sh"]:
        out, err, rc = middleman.pexec(["sh", script])
        if rc != 0:
            sys.exit(f"failed to run {script}: {err}")

    for side in ['inner', 'outer']:
        for node in range(3):
            net.nameToNode[f'{side}node{node}'].cmd('ip route add 192.168.3.0/24 via 192.168.2.1')

    try:
        CLI(net)
    finally:
        net.stop()
