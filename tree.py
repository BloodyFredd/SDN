from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from mininet.topo import Topo

def treeTopo():
    #net = Mininet( controller=RemoteController )
    net = Mininet(topo=topo,controller=lambda name:RemoteController(name,ip='127.0.0.1', protocol='tcp',port=6633) , link=TCLink)
    
    info( '*** Adding controller\n' )
    net.addController('c0')
    
    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
    h2 = net.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
    h3 = net.addHost( 'h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
    h4 = net.addHost( 'h4', ip='10.0.0.4', mac='00:00:00:00:00:04' )
    #h5 = net.addHost( 'h5', ip='10.0.0.5', mac='00:00:00:00:00:05' )
    #h6 = net.addHost( 'h6', ip='10.0.0.6', mac='00:00:00:00:00:06' )
    #h7 = net.addHost( 'h7', ip='10.0.0.7', mac='00:00:00:00:00:07' )
    #h8 = net.addHost( 'h8', ip='10.0.0.8', mac='00:00:00:00:00:08' )

    info( '*** Adding switches\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    #s5 = net.addSwitch( 's5' )
    #s6 = net.addSwitch( 's6' )
    #s7 = net.addSwitch( 's7' )
    
    info( '*** Creating links\n' )
    net.addLink( h1, s1, port1=3)
    net.addLink( h2, s1, port1=4)

    net.addLink( h3, s4, port1=3)
    net.addLink( h4, s4, port1=4)

    #l1 = [s1,s2]
    #l2 = [s3,s4]
    
    net.addLink( s1 , s2 , port1=1, port2=1, bw=1) 
    net.addLink( s1 , s3 , port1=2, port2=1, bw=10) 
    net.addLink( s2 , s4 , port1=2, port2=1, bw=1) 
    net.addLink( s3 , s4 , port1=2, port2=2, bw=10)     
    
    info( '*** Starting network\n')
    net.start()
    
    info( '*** Running CLI\n' )
    CLI( net )
    
    info( '*** Stopping network' )
    net.stop()
    
if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
