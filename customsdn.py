#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.node import CPULimitedHost, Host, Node, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link, Intf
from subprocess import call

def myNetwork():

    net = Mininet(switch=OVSKernelSwitch, link=TCLink, topo=None)
    queue1=5
    queue2=3
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', mac='00:00:00:00:00:01', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', mac='00:00:00:00:00:02', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', mac='00:00:00:00:00:03', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', mac='00:00:00:00:00:04', protocols='OpenFlow13')
    s5 = net.addSwitch('s5', mac='00:00:00:00:00:05', protocols='OpenFlow13')
    s6 = net.addSwitch('s6', mac='00:00:00:00:00:06', protocols='OpenFlow13')
    s7 = net.addSwitch('s7', mac='00:00:00:00:00:07', protocols='OpenFlow13')
    s8 = net.addSwitch('s8', mac='00:00:00:00:00:08', protocols='OpenFlow13')

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

    c0=net.addController('c0',controller=RemoteController,ip='127.0.0.1',port=6633)


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
    c0.start()
    net.get('s5').start([c0])
    net.get('s1').start([c0])
    net.get('s4').start([c0])
    net.get('s7').start([c0])
    net.get('s2').start([c0])
    net.get('s6').start([c0])
    net.get('s8').start([c0])
    net.get('s3').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

