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
        h1 = self.addHost( 'h1')
        h2 = self.addHost( 'h2')
        s1 = self.addSwitch('s1')
 
        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )


topos = { 'mytopo': ( lambda: MyTopo() ) }

# sudo mn --custom ~/server1.py --controller=remote,ip=192.168.99.1
# mininet> h1 ifconfig h1-eth0 10.0.0.1
# mininet> h1 ip link set h1-eth0 address 00:00:00:00:00:01 
# mininet> h2 ifconfig h2-eth0 10.0.0.2
# mininet> h2 ip link set h2-eth0 address 00:00:00:00:00:02 
