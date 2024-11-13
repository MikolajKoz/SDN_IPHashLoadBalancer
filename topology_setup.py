from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__( self ):
        Topo.__init__( self )
        # Initialize topology
        # Add hosts and switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        l1 = self.addSwitch( 'l1' )
        l2 = self.addSwitch( 'l2' )
        l3 = self.addSwitch( 'l3' )
        l4 = self.addSwitch( 'l4' )
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )

        # Add links
        for leaf in [l1, l2, l3, l4]:
            self.addLink(leaf, s1)
            self.addLink(leaf, s2)

        self.addLink(l1, h1)
        self.addLink(l1, h2)
        self.addLink(l2, h3)
        self.addLink(l2, h4)


topos = { 'mytopo': ( lambda: MyTopo() ) }