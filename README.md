This repository accompanies my answer to <https://unix.stackexchange.com/q/735931/4989>.

## Requirements

You'll need [Mininet](http://mininet.org/). The easiest way to use this is to download the [mininet vm](http://mininet.org/download/).

## How to use these files

To deploy a virtual network with the routing and netfilter configuration applied:

```
sudo python network.py
```

To deploy a virtual network with the topology in place but without any routing or netfilter configuration:

```
sudo mn --custom topology.py --topo custom
```

## Topology

[![topology diagram][1]][1]

[1]: https://www.plantuml.com/plantuml/svg/7Sn12i9034RXlQVG0qo3515TzIgn3UrW9ZDC_c2zlLJUuks-oS4TKVHqoJPhB7BUWEPFeZLZYzSmrqBAtTzEONbFidDfAka-tXxZDHqPWpf_gB13Eg6sgdNz3atP_lOajXp_0G00

