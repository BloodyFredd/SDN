from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.node import RemoteController

class Topology(Topo):
    def __init__(self):
        Topo.__init__(self)

	# Building the topology.
    def build(self):    
	    #Adding hosts
	    h1 = self.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
	    h2 = self.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
	    h3 = self.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
	    h4 = self.addHost('h4', ip='10.0.0.4', mac='00:00:00:00:00:04' )

	    #Adding switches
	    s1 = self.addSwitch('s1')
	    s2 = self.addSwitch('s2')
	    s3 = self.addSwitch('s3')
	    s4 = self.addSwitch('s4')
	    
	    #Creating Links between hosts and switches	    
	    self.addLink(h1, s1, port1=1, port2=3)
	    self.addLink(h2, s1, port1=1, port2=4)
	    
	    self.addLink(s1 , s2 , port1=1, port2=1, bw=1) 	    
	    self.addLink(s2 , s4 , port1=2, port2=1, bw=1)
	     
	    self.addLink(s1 , s3 , port1=2, port2=1, bw=10)  
	    self.addLink(s3 , s4 , port1=2, port2=2, bw=10) 

	    self.addLink(h3, s4, port1=1, port2=3)
	    self.addLink(h4, s4, port1=1, port2=4)	 

topo = Topology()
# Start the mininet topology we built.
net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', protocol='tcp', port = 6633), link=TCLink)
net.start()
CLI(net)
net.stop()


