from mininet.topo import Topo

class Custom(Topo):
    def build(self):
        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')

        middleman = self.addHost('middleman', ip='192.168.2.1/24')
        self.addLink(middleman, s0)
        self.addLink(middleman, s1, params1=dict(ip='192.168.2.1/24'))

        for side in ['inner', 'outer']:
            switch = {'inner': s0, 'outer': s1}[side]

            for node in range(3):
                node = self.addHost(f'{side}node{node}', ip=f'192.168.2.{10+node}/24')
                self.addLink(node, switch)


topos = {"custom": Custom}
