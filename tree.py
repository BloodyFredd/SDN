#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.topo import Topo

class Topology(Topo):
	def __init__(self):
		Topo.__init__(self)

	def build(self):
	    info( '*** Adding hosts \n' )
	    h1 = self.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
	    h2 = self.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
	    h3 = self.addHost( 'h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
	    h4 = self.addHost( 'h4', ip='10.0.0.4', mac='00:00:00:00:00:04' )

	    info( '*** Adding switches\n' )
	    s1 = self.addSwitch( 's1')
	    s2 = self.addSwitch( 's2')
	    s3 = self.addSwitch( 's3')
	    s4 = self.addSwitch( 's4')
	    
	    
	    info( '*** Creating links\n' )
	    self.addLink( h1, s1, port1=0, port2=3)
	    self.addLink( h2, s1, port1=0, port2=4)

	    self.addLink( h3, s4, port1=0, port2=3)
	    self.addLink( h4, s4, port1=0, port2=4)
	    
	    self.addLink( s1 , s2 , port1=1, port2=1, bw=1) 
	    self.addLink( s1 , s3 , port1=2, port2=1, bw=10) 

	    self.addLink( s2 , s4 , port1=2, port2=1, bw=1) 
	    self.addLink( s3 , s4 , port1=2, port2=2, bw=10)  


#def treeTopo():
    
    #net = Mininet(topo=topo,controller=lambda name:RemoteController(name,ip='127.0.0.1', 	    protocol='tcp',port=6633) , link=TCLink)
    
    #info( '*** Adding controller\n' )
#    net.addController('c0')
    
#    info( '*** Adding hosts\n' )
#    h1 = net.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
#    h2 = net.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
#    h3 = net.addHost( 'h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
#    h4 = net.addHost( 'h4', ip='10.0.0.4', mac='00:00:00:00:00:04' )

#    info( '*** Adding switches\n' )
#    s1 = net.addSwitch( 's1', dpid=1)
#    s2 = net.addSwitch( 's2', dpid=2)
#    s3 = net.addSwitch( 's3', dpid=3)
#    s4 = net.addSwitch( 's4', dpid=4)
    
#   info( '*** Creating links\n' )
#    net.addLink( h1, s1, port1=0, port2=3)
#    net.addLink( h2, s1, port1=0, port2=4)

#    net.addLink( h3, s4, port1=0, port2=3)
#    net.addLink( h4, s4, port1=0, port2=4)
    
#    net.addLink( s1 , s2 , port1=1, port2=1, bw=1) 
#    net.addLink( s1 , s3 , port1=2, port2=1, bw=10) 

#    net.addLink( s2 , s4 , port1=2, port2=1, bw=1) 
#    net.addLink( s3 , s4 , port1=2, port2=2, bw=10)     

topo = Topology()

#net = Mininet( controller=RemoteController )	   
net = Mininet(topo=topo,controller=lambda name:RemoteController(name,ip='127.0.0.1', 	  protocol='tcp',port=6633) , link=TCLink)
    
info( '*** Starting network\n')
net.start()
    
info( '*** Running CLI\n' )
CLI( net )
    
info( '*** Stopping network' )
net.stop()
    
#if __name__ == '__main__':
#    setLogLevel( 'info' )
#    treeTopo()
