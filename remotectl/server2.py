"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h3 = self.addHost( 'h3')
        h4 = self.addHost( 'h4')
        s2 = self.addSwitch('s2')
 
        # Add links
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

# sudo mn --custom ~/server2.py --controller=remote,ip=192.168.99.1
# mininet> h3 ifconfig h3-eth0 10.0.0.3
# mininet> h3 ip link set h3-eth0 address 00:00:00:00:00:03 
# mininet> h4 ifconfig h4-eth0 10.0.0.4
# mininet> h4 ip link set h4-eth0 address 00:00:00:00:00:04 
