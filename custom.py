#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link, Intf
from subprocess import call

def myNetwork():

    net = Mininet(controller=None, link=TCLink, topo=None)
    queue1=10
    queue2=5
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', mac='00:00:00:00:00:01', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s2 = net.addSwitch('s2', mac='00:00:00:00:00:02', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s3 = net.addSwitch('s3', mac='00:00:00:00:00:03', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s4 = net.addSwitch('s4', mac='00:00:00:00:00:04', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s5 = net.addSwitch('s5', mac='00:00:00:00:00:05', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s6 = net.addSwitch('s6', mac='00:00:00:00:00:06', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s7 = net.addSwitch('s7', mac='00:00:00:00:00:07', cls=OVSKernelSwitch, failMode='standalone', stp=True)
    s8 = net.addSwitch('s8', mac='00:00:00:00:00:08', cls=OVSKernelSwitch, failMode='standalone', stp=True)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, mac='00:00:00:00:10:01', ip='10.0.10.1/8', defaultRoute='via 10.100.0.1')
    h2 = net.addHost('h2', cls=Host, mac='00:00:00:00:20:01', ip='10.0.20.1/8', defaultRoute='via 10.100.0.1')
    h3 = net.addHost('h3', cls=Host, mac='00:00:00:00:30:01', ip='10.0.30.1/8', defaultRoute='via 10.100.0.1')
    h4 = net.addHost('h4', cls=Host, mac='00:00:00:00:40:01', ip='10.0.40.1/8', defaultRoute='via 10.100.0.1')
    h5 = net.addHost('h5', cls=Host, mac='00:00:00:00:50:01', ip='10.0.50.1/8', defaultRoute='via 10.100.0.1')
    h6 = net.addHost('h6', cls=Host, mac='00:00:00:01:10:01', ip='20.0.10.1/8', defaultRoute='via 20.100.0.1')
    h7 = net.addHost('h7', cls=Host, mac='00:00:00:01:20:01', ip='20.0.20.1/8', defaultRoute='via 20.100.0.1')
    h8 = net.addHost('h8', cls=Host, mac='00:00:00:01:30:01', ip='20.0.30.1/8', defaultRoute='via 20.100.0.1')
    h9 = net.addHost('h9', cls=Host, mac='00:00:00:01:40:01', ip='20.0.40.1/8', defaultRoute='via 20.100.0.1')
    h10 = net.addHost('h10', cls=Host, mac='00:00:00:01:50:01', ip='20.0.50.1/8', defaultRoute='via 20.100.0.1')
    r = net.addHost('r', cls=Host, mac='10:10:10:10:10:01', ip='10.100.0.1')


    info( '*** Add links\n')
    net.addLink(s3, s4, bw=50, delay='3ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s4, s2, bw=60, delay='5ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s2, s1, bw=70, delay='10ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s1, s4, bw=50, delay='1ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s3, s2, bw=70, delay='10ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s2, s5, bw=60, delay='8ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s5, s6, bw=50, delay='4ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s5, s4, bw=80, delay='8ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s4, s6, bw=60, delay='5ms', max_queue_size=queue1, use_tbf=True)
    net.addLink(s6, s2, bw=70, delay='10ms', max_queue_size=queue1, use_tbf=True)
    Link(r, s5, intfName1='r-eth0')
    Link(r, s7, intfName1='r-eth1')
    #net.addLink(r, s5)
    #net.addLink(r, s7)
    r.cmd('ifconfig r-eth1 20.100.0.1 netmask 255.0.0.0')
    r.cmd('sysctl -w net.ipv4.ip_forward=1')
    net.addLink(s7, s8, bw=25, delay='4ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h1, s1, bw=30, delay='1ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h2, s1, bw=40, delay='2ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h3, s2, bw=10, delay='5ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h4, s2, bw=15, delay='7ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h5, s2, bw=80, delay='8ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h6, s8, bw=50, delay='5ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h7, s8, bw=10, delay='4ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h8, s8, bw=5, delay='2ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h9, s8, bw=100, delay='3ms', max_queue_size=queue2, use_tbf=True)
    net.addLink(h10, s8, bw=20, delay='4ms', max_queue_size=queue2, use_tbf=True)

    info( '*** Starting network\n')
    net.build()

    info( '*** Starting switches\n')
    net.get('s5').start([])
    net.get('s1').start([])
    net.get('s4').start([])
    net.get('s7').start([])
    net.get('s2').start([])
    net.get('s6').start([])
    net.get('s8').start([])
    net.get('s3').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

